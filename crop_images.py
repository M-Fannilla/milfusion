import json
import shutil
import pandas as pd
from tqdm import tqdm
from PIL import Image
from pathlib import Path
from utils import SRC_DIR, BUCKET
from concurrent.futures import ThreadPoolExecutor, as_completed

df = pd.read_csv('datasets/medium_one_hot.csv.csv')

all_blobs = [Path(B) for B in df['file_path'].tolist()]
print("Total blobs:", len(all_blobs))


def crop_image_and_save(local_image_path: Path, vertices: list) -> Path | None:
    try:
        y_vertices = [int(vertex['y']) for vertex in vertices]
        upper = min(y_vertices)
        lower = max(y_vertices)

        image = Image.open(local_image_path)
        width, height = image.size

        if abs(lower - upper) > 0.25 * height:
            return

        if upper < height / 2:
            cropped_image = image.crop(
                (0, lower, width, height)  # (left, upper, right, and lower)
            )

        else:
            cropped_image = image.crop(
                (0, 0, width, upper)  # (left, upper, right, and lower)
            )

        local_image_path = Path(local_image_path).parent / "cropped" / Path(local_image_path).name
        local_image_path.parent.mkdir(parents=True, exist_ok=True)
        cropped_image.save(local_image_path)
        return local_image_path

    except Exception as e:
        return None


def crop_process(image_file_path: Path, force: bool = True):
    local_image_path = (
            SRC_DIR / image_file_path
    )
    local_crop_image_path = (
            SRC_DIR / image_file_path.parent.as_posix() / 'cropped' / f"{image_file_path.name}"
    )
    gcp_crop_image_path = (
        f"pics/{image_file_path.parent.as_posix()}/cropped/{image_file_path.name}"
    )

    if BUCKET.blob(gcp_crop_image_path).exists() and not force:
        if local_crop_image_path.exists():
            return

        else:
            BUCKET.blob(gcp_crop_image_path).download_to_filename(local_crop_image_path)
            return

    else:
        if local_crop_image_path.exists() and not force:
            BUCKET.blob(gcp_crop_image_path).upload_from_filename(local_crop_image_path.as_posix())
            return

        else:
            local_vertices_path = SRC_DIR / image_file_path.parent.as_posix() / 'cropped' / f"{image_file_path.with_suffix('').name}.json"
            with open(local_vertices_path, 'r') as json_file:
                vertices = json.load(json_file)

            if isinstance(vertices, list):
                true_crop_image_path = crop_image_and_save(local_image_path, vertices)
                if true_crop_image_path:
                    BUCKET.blob(gcp_crop_image_path).upload_from_filename(true_crop_image_path.as_posix())
                else:
                    return

            if vertices is None:
                shutil.copy(local_image_path, local_crop_image_path)
                BUCKET.blob(gcp_crop_image_path).upload_from_filename(local_image_path.as_posix())

            else:
                return


if __name__ == '__main__':
    futures = []

    with ThreadPoolExecutor(max_workers=16) as executor:
        for blob in tqdm(all_blobs, total=len(all_blobs), desc="Collecting images"):
            futures.append(
                executor.submit(crop_process, blob, True)
            )

        for future in tqdm(as_completed(futures), total=len(futures), desc="Processing images"):
            pass
