import shutil
from pathlib import Path

import pandas as pd
from tqdm import tqdm
import multiprocessing
from utils import SRC_DIR, BUCKET
from concurrent.futures import ThreadPoolExecutor

dataset_name = "cropped_all_one_hot"
df = pd.read_csv(f"datasets/{dataset_name}.csv", index_col=0)
filenames = df["file_path"].tolist()
IMAGE_DIR = Path("./images")


def main_process(file_name: str, preserve_structure: bool = False, force_download: bool = False):
    gcp_file_path = "pics/" + file_name
    local_destination = IMAGE_DIR / file_name if preserve_structure else IMAGE_DIR / file_name.split("/")[-1]

    if local_destination.exists() and not force_download:
        return

    local_destination.parent.mkdir(parents=True, exist_ok=True)
    BUCKET.blob(gcp_file_path).download_to_filename(local_destination.as_posix())


def main_process_from_drive(file_name: str, preserve_structure: bool = False, force_download: bool = False):
    source_path = SRC_DIR / file_name
    target_path = IMAGE_DIR / file_name if preserve_structure else IMAGE_DIR / file_name.split("/")[-1]
    if target_path.exists() and not force_download:
        return
    target_path.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy(source_path, target_path)


if __name__ == "__main__":
    force = False
    structure = False

    with ThreadPoolExecutor(max_workers=multiprocessing.cpu_count() * 2) as executor:
        results = [
            executor.submit(main_process, filename, structure, force)
            for filename in tqdm(filenames, desc="Submitting process...", total=len(filenames))
        ]

        for result in tqdm(results, total=len(results), desc="Downloading images"):
            result.result()
    print("Compiling dataset...")
    _out_df = df.copy()
    _out_df["file_path"] = _out_df["file_path"].apply(lambda x: IMAGE_DIR / x.split("/")[-1])
    _out_df.to_csv(f"{IMAGE_DIR.as_posix()}/compiled_{dataset_name}.csv")
    # print(f"Archiving {IMAGE_DIR}...")
    # shutil.make_archive(IMAGE_DIR.as_posix(), 'zip', IMAGE_DIR)
    print("Done")
