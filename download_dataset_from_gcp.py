import pandas as pd
from tqdm import tqdm
import multiprocessing
from utils import SRC_DIR, BUCKET
from concurrent.futures import ThreadPoolExecutor

filenames = pd.read_csv("datasets/cropped_medium_one_hot.csv")["file_path"].tolist()


def main_process(file_name: str):
    gcp_file_path = "pics/" + file_name
    destination = SRC_DIR / file_name
    if destination.exists():
        return
    destination.parent.mkdir(parents=True, exist_ok=True)
    BUCKET.blob(gcp_file_path).download_to_filename(destination.as_posix())


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=multiprocessing.cpu_count() * 2) as executor:
        results = [
            executor.submit(main_process, filename)
            for filename in filenames
        ]

        for result in tqdm(results, total=len(results), desc="Downloading images"):
            result.result()
