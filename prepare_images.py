import multiprocessing
import os
import concurrent
import pandas as pd
from tqdm import tqdm
from google.cloud import storage
from concurrent.futures import ThreadPoolExecutor

BUCKET_NAME = 'chum_bucket_stuff'
TARGET_DIR = './images'

if not os.path.exists(TARGET_DIR):
    os.makedirs(TARGET_DIR)


def download_file(file_path):
    client = storage.Client()
    bucket = client.bucket(BUCKET_NAME)
    blob = bucket.blob(f"pics/{file_path}")
    destination_path = os.path.join(TARGET_DIR, os.path.basename(file_path.split("/")[-1]))
    blob.download_to_filename(destination_path)


def download_files_from_dataframe(dataframe):
    file_paths = dataframe['file_path'].tolist()

    with ThreadPoolExecutor(max_workers=multiprocessing.cpu_count() - 2) as executor:
        futures = [
            executor.submit(download_file, file_path)
            for file_path in file_paths
        ]

        for future in tqdm(concurrent.futures.as_completed(futures)):
            future.result()


if __name__ == "__main__":
    df = pd.read_csv('sample_df.csv')
    download_files_from_dataframe(df)
