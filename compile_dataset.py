import shutil

import pandas as pd
from tqdm import tqdm
import multiprocessing
from utils import SRC_DIR, BUCKET
from concurrent.futures import ThreadPoolExecutor

df = pd.read_csv("datasets/cropped_medium_one_hot.csv")
filenames = df["file_path"].tolist()


def main_process(file_name: str, preserve_structure: bool = False):
    gcp_file_path = "pics/" + file_name
    local_destination = SRC_DIR / file_name if preserve_structure else SRC_DIR / file_name.split("/")[-1]

    if not local_destination.exists():
        local_destination.parent.mkdir(parents=True, exist_ok=True)
        BUCKET.blob(gcp_file_path).download_to_filename(local_destination.as_posix())


def main_process_from_drive(file_name: str, preserve_structure: bool = False):
    source_path = SRC_DIR / file_name
    target_path = SRC_DIR / file_name if preserve_structure else SRC_DIR / file_name.split("/")[-1]
    target_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(source_path, target_path)


if __name__ == "__main__":
    structure = False

    with ThreadPoolExecutor(max_workers=multiprocessing.cpu_count() * 2) as executor:
        results = [
            executor.submit(main_process, filename, structure)
            for filename in filenames
        ]

    for result in tqdm(results, total=len(results), desc="Downloading images"):
        result.result()
