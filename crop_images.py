import json
import pandas as pd
from tqdm import tqdm
from PIL import Image
from pathlib import Path
from utils import SRC_DIR, BUCKET
from concurrent.futures import ThreadPoolExecutor, as_completed

df = pd.read_csv('datasets/medium_one_hot.csv')

all_blobs = [Path(B) for B in df['file_path'].tolist()]
print("Total blobs:", len(all_blobs))


def crop_image(local_image_path: Path, vertices: list) -> Path | None:
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


def crop_process(image_file_path: Path):
    print("Image:", image_file_path)
    local_vertices_path = (
            SRC_DIR / image_file_path.parent.as_posix() / 'cropped' / f"{image_file_path.with_suffix('').name}.json"
    )
    print("Local_vPath:", local_vertices_path)

    with open(local_vertices_path, 'w') as json_file:
        vertices = json.load(json_file)
        if not vertices:
            return

    print("Vertices:", vertices)
    if BUCKET.blob(image_file_path.as_posix()).exists():
        if not image_file_path.exists():
            BUCKET.blob(image_file_path.as_posix()).download_to_filename(image_file_path)

    # if image_file_path.exists():
    #     BUCKET.blob(
    #         image_file_path.as_posix()
    #     ).upload_from_filename(
    #         image_file_path.as_posix()
    #     )
    #
    #
    # else:
    #     cropped_image_path = crop_image(image_file_path, vertices)
    #
    #     if cropped_image_path:
    #         BUCKET.blob(
    #             cropped_image_path.as_posix()
    #         ).upload_from_filename(
    #             cropped_image_path.as_posix()
    #         )


if __name__ == '__main__':
    crop_process(all_blobs[0])
    # futures = []
    # try:
    #     with ThreadPoolExecutor(max_workers=16) as executor:
    #         for i, blob in enumerate(all_blobs):
    #             futures.append(executor.submit(crop_process, blob))
    #
    #         for future in tqdm(as_completed(futures), total=len(futures), desc="Processing images"):
    #             future.result()
    #
    # except Exception as e:
    #     print(">>> Interrupted <<<")
    #
    # finally:
    #     print(
    #         "Total number of blobs processed:", len(all_blobs)
    #     )
