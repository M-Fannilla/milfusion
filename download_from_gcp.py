import os
import concurrent
from tqdm import tqdm
from pathlib import Path
from google.cloud import storage
from concurrent.futures import ThreadPoolExecutor

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/teamspace/uploads/fannilla-cfd25ffd1b7c.json"

BUCKET_NAME = 'pornpics_scrape'
CLIENT = storage.Client()
BUCKET = CLIENT.bucket(BUCKET_NAME)
DESTINATION_FOLDER = "./images"

CATEGORIES = [
        'amateur', 'bath', 'big-tits', 'bikini', 'blonde', 'boots', 'brunette', 'centerfold', 'christmas', 
        'chubby', 'clothed', 'cougar', 'curvy', 'doggystyle', 'face', 'fake-tits', 'feet', 'glasses', 'granny', 
        'hairy', 'high-heels', 'homemade', 'housewife', 'jeans', 'legs', 'lingerie', 'maid', 'masturbation', 'mature', 
        'milf', 'model', 'mom', 'natural-tits', 'non-nude', 'nude', 'nurse', 'office', 'panties', 'pantyhose', 'pool', 
        'pornstar', 'redhead', 'saggy-tits', 'secretary', 'selfie', 'sexy', 'shaved', 'short-hair', 'shorts', 'skinny', 
        'skirt', 'smoking', 'socks', 'solo', 'spreading', 'stockings', 'thick', 'thong', 'undressing', 'upskirt', 'white'
    ]

BUCKET_NAME = 'pornpics_scrape'


def fetch_all_blobs(folder_prefix: str = None):
    """Fetch all file paths from the GCS bucket."""
    blobs = BUCKET.list_blobs(prefix=folder_prefix)
    return [blob.name for blob in blobs]


def download_category(category_blobs, destination_folder, force_download):
    """Download a blob from the GCS bucket."""

    def _download_blob(b):
        file_path = Path(destination_folder) / b
        file_path.parent.mkdir(parents=True, exist_ok=True)
        if not force_download and file_path.exists():
            return
        BUCKET.blob(b).download_to_filename(file_path.as_posix())

    with ThreadPoolExecutor() as executor:
        futures = [executor.submit(_download_blob, b) for b in category_blobs]
        for _ in tqdm(
            concurrent.futures.as_completed(futures), 
            total=len(futures), 
            desc=f"Downloading Blobs {category_blobs[0].split('/')[0]}"
            ):
            pass

if __name__ == "__main__":
    for category in CATEGORIES:
        category_blobs = fetch_all_blobs(folder_prefix=category)
        download_category(
            category_blobs=category_blobs,
            destination_folder=DESTINATION_FOLDER,
            force_download=False
        )
