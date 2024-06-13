import os
import multiprocessing
from pathlib import Path
from google.cloud import storage

from concurrent.futures import ThreadPoolExecutor

client = storage.Client()
SRC_DIR = Path("/Volumes/external_drive")
_bucket = client.bucket("chum_bucket_stuff")


def upload_file(local_file_path, gcp_file_path):
    blob = _bucket.blob(gcp_file_path)
    blob.upload_from_filename(local_file_path)


def upload_folders_to_gcp():
    with ThreadPoolExecutor(max_workers=(multiprocessing.cpu_count() * 2) - 1) as executor:
        futures = []

        for category in os.listdir(SRC_DIR):
            local_folder_path = SRC_DIR / category

            for root, _, files in os.walk(local_folder_path):
                for file in files:
                    if file.endswith("gallery_info.txt"):
                        local_path = os.path.join(root, file)
                        gcp_path = local_path.replace(str(SRC_DIR), "pics")
                        print(f"Uploading from {local_path} to {gcp_path}")
                        futures.append(executor.submit(upload_file, local_path, gcp_path))

        for future in futures:
            future.result()


if __name__ == "__main__":
    upload_folders_to_gcp()