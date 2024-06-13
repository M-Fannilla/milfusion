import pandas as pd
from tqdm import tqdm
import multiprocessing
from utils import SRC_DIR, BUCKET
from concurrent.futures import ThreadPoolExecutor

filenames = pd.read_csv("datasets/cropped_medium_one_hot.csv")["file_path"].tolist()


def main_process(file_name: str, preserve_structure: bool = False):
    gcp_file_path = "pics/" + file_name
    local_destination = SRC_DIR / file_name if preserve_structure else SRC_DIR / file_name.split("/")[-1]

    # print("Destination:", local_destination)
    # print("GCP File Path:", gcp_file_path)

    if not local_destination.exists():
        local_destination.parent.mkdir(parents=True, exist_ok=True)
        BUCKET.blob(gcp_file_path).download_to_filename(local_destination.as_posix())


if __name__ == "__main__":
    with ThreadPoolExecutor(max_workers=multiprocessing.cpu_count() * 2) as executor:
        results = [
            executor.submit(main_process, filename, False)
            for filename in filenames[:100]
        ]

        for result in tqdm(results, total=len(results), desc="Downloading images"):
            result.result()
