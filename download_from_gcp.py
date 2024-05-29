import os
import concurrent
from tqdm import tqdm
from pathlib import Path
from google.cloud import storage
import multiprocessing
from concurrent.futures import ThreadPoolExecutor, ProcessPoolExecutor
from tqdm import tqdm
import concurrent.futures

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

def download_blob(b, destination_folder, force_download, pbar):
    """Download a blob from the GCS bucket."""
    file_path = Path(destination_folder) / b
    file_path.parent.mkdir(parents=True, exist_ok=True)
    if not force_download and file_path.exists():
        pbar.update(1)
        return
    BUCKET.blob(b).download_to_filename(file_path.as_posix())
    pbar.update(1)

def download_category(category_blobs, destination_folder, force_download, pbar_position):
    """Download a category of blobs from the GCS bucket."""
    with tqdm(total=len(category_blobs), desc=f"Category {category_blobs[0].split('/')[0]}", position=pbar_position) as pbar:
        with ThreadPoolExecutor() as executor:
            futures = [executor.submit(download_blob, b, destination_folder, force_download, pbar) for b in category_blobs]
            for future in concurrent.futures.as_completed(futures):
                future.result()  # To raise any exceptions

if __name__ == "__main__":
    manager = multiprocessing.Manager()
    with ProcessPoolExecutor(max_workers=32) as executor:
        futures = [
            executor.submit(download_category, fetch_all_blobs(folder_prefix=category), DESTINATION_FOLDER, False, i) 
            for i, category in enumerate(CATEGORIES)
        ]
        
        for _ in concurrent.futures.as_completed(futures):
            pass