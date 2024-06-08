import pandas as pd
from tqdm import tqdm
from pathlib import Path
from google.cloud import storage
from concurrent.futures import ThreadPoolExecutor

BUCKET_NAME = 'chum_bucket_stuff'
CLIENT = storage.Client()

BUCKET = CLIENT.bucket(BUCKET_NAME)
DESTINATION_FOLDER = Path("./images")

filenames = pd.read_csv("datasets/ai_gen_dataset_10_cats.csv")["file_path"].tolist()


def main_process(file_name: str):
    gcp_file_path = "pics/" + file_name
    destination = DESTINATION_FOLDER / file_name
    if destination.exists():
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    BUCKET.blob(gcp_file_path).download_to_filename(destination.as_posix())


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=32) as executor:
        results = [
            executor.submit(main_process, filename)
            for filename in filenames
        ]

        for result in tqdm(results, total=len(results), desc="Downloading images"):
            result.result()
