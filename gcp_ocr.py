import os
import re
import json
import time
import pandas as pd
from tqdm import tqdm
from pathlib import Path
from google.cloud import vision
from google.cloud import storage
from concurrent.futures import ThreadPoolExecutor, as_completed

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "fannilla-dev.json"

vision_client = vision.ImageAnnotatorClient()
storage_client = storage.Client()

BUCKET_NAME = 'chum_bucket_stuff'
SRC_DIR = Path("/Volumes/external_drive")

BUCKET = storage_client.bucket(BUCKET_NAME)

df = pd.read_csv('datasets/images_high_res_dataset.csv')
df.sort_values(by=['gallery_category', 'gallery_name'], inplace=True)

df['blobs'] = df.apply(
    lambda x: f"pics/{x['gallery_category']}/{x['gallery_name']}/{x['filename']}", axis=1
)
all_blobs = [Path(B) for B in df['blobs'].tolist()]
print("Total blobs:", len(all_blobs), f"\n{all_blobs[:1]}")


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


def get_vertices_from_response(
        response: vision.AnnotateImageResponse
) -> list[dict[str, int]]:
    if not response.text_annotations:
        return None

    bounding_poly = response.text_annotations[0].bounding_poly
    vertices = str(bounding_poly.vertices)

    return convert_string_to_vertices_list(vertices)


def ocr_process(blob_name: Path):
    cropped_file_path = blob_name.parent / 'cropped' / blob_name.name
    print("Cropped file path:", cropped_file_path)
    vertices_path = (
            SRC_DIR
            / cropped_file_path.parent.as_posix().replace("pics/", '')
            / f"{cropped_file_path.with_suffix('').name}.json"
    )

    print("Vertices path:", vertices_path)
    cropped_file_path.parent.mkdir(parents=True, exist_ok=True)

    if not vertices_path.exists():
        gcp_file = f"gs://{BUCKET_NAME}/{blob_name.as_posix()}"
        print("GCP file:", gcp_file)

        # response = request_ocr(gcp_file)
        # vertices = get_vertices_from_response(response)
        #
        # if vertices:  # If OCR found vertices
        #     with open(vertices_path, 'w') as json_file:
        #         json.dump(vertices, json_file, indent=4)


def filter_blob_categories(categories: list[str]):
    out = []
    for blob in all_blobs:
        for category in categories:
            if f"/{category}/" in blob.as_posix():
                out.append(blob)
    return out


if __name__ == '__main__':
    cats = ['mature', ]
    for blob in filter_blob_categories(cats)[:1]:
        ocr_process(blob)

    # with ThreadPoolExecutor(max_workers=10) as executor:
    #     futures = [
    #         executor.submit(ocr_process, blob)
    #         for blob in filter_blob_categories(cats)
    #     ]
    #     for future in as_completed(futures):
    #         future.result()
