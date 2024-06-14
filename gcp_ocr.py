import re
import json
import time
import pandas as pd
from tqdm import tqdm
from pathlib import Path
from google.cloud import vision
from utils import vision_client, SRC_DIR, BUCKET
from concurrent.futures import ThreadPoolExecutor, as_completed

df = pd.read_csv('datasets/all_one_hot.csv', index_col=0)

all_blobs = [Path(B) for B in df['file_path'].tolist()]
print("Total blobs:", len(all_blobs))


def filter_blob_categories(categories: list[str]):
    out = []
    for blob in all_blobs:
        for category in categories:
            if f"/{category}/" in blob.as_posix():
                out.append(blob)
    return out


def request_ocr(blob_location: str) -> vision.AnnotateImageResponse:
    image = vision.Image()
    image.source.image_uri = blob_location
    request = {
        "image": image,
        "features": [
            {
                "type_": vision.Feature.Type.TEXT_DETECTION
            }
        ],
    }
    return vision_client.annotate_image(request)


def convert_string_to_vertices_list(vertices_string):
    pattern = re.compile(r'x:\s*(\d+)\s*y:\s*(\d+)')
    matches = pattern.findall(vertices_string)
    return [{'x': int(x), 'y': int(y)} for x, y in matches]


def get_vertices_from_response(response: vision.AnnotateImageResponse) -> list[dict[str, int]] | None:
    if not response.text_annotations:
        return None

    bounding_poly = response.text_annotations[0].bounding_poly
    vertices = str(bounding_poly.vertices)

    return convert_string_to_vertices_list(vertices)


def ocr_process(blob_name: Path):
    gcp_vertices_path = (
        f"pics/{blob_name.parent.as_posix()}/cropped/{blob_name.with_suffix('').name}.json"
    )

    local_vertices_path = (
            SRC_DIR / blob_name.parent.as_posix() / 'cropped' / f"{blob_name.with_suffix('').name}.json"
    )

    local_vertices_path.parent.mkdir(parents=True, exist_ok=True)

    if BUCKET.blob(gcp_vertices_path).exists():
        if not local_vertices_path.exists():
            BUCKET.blob(gcp_vertices_path).download_to_filename(local_vertices_path)
            # print("Downloaded from GCP to:", local_vertices_path.as_posix())
        else:
            pass
            # print("Already exists on GCP and locally.")
    else:
        # print("Does not exist on GCP:", gcp_vertices_path)
        if not local_vertices_path.exists():
            # print("Does not exist locally:", local_vertices_path.as_posix())
            response = request_ocr(
                f"gs://{BUCKET.name}/pics/{blob_name.as_posix()}"
            )
            vertices = get_vertices_from_response(response)
            # print("Vertices:", vertices)
            with open(local_vertices_path, 'w') as json_file:
                json.dump(vertices, json_file, indent=4)
        else:
            pass
            # print("Already exists locally.")

        BUCKET.blob(gcp_vertices_path).upload_from_filename(local_vertices_path)


if __name__ == '__main__':
    pause = 60
    futures = []
    try:
        with ThreadPoolExecutor(max_workers=16) as executor:
            for i, blob in enumerate(all_blobs):
                futures.append(executor.submit(ocr_process, blob))
                if i != 0 and i % 1700 == 0:
                    for future in tqdm(as_completed(futures), total=len(futures), desc="Processing images"):
                        future.result()
                    start = time.time()
                    print("Sleeping.", end="")
                    while time.time() - start <= pause:
                        time.sleep(2)
                        print(".", flush=True, end="")

            for future in tqdm(as_completed(futures), total=len(futures), desc="Processing images"):
                future.result()

    except Exception as e:
        print(">>> Interrupted <<<\n", e)

    finally:
        print(
            "Total number of blobs processed:", len(all_blobs)
        )
