import asyncio
from tqdm import tqdm
from typing import List
from pathlib import Path
from google.cloud import storage
from concurrent.futures import ThreadPoolExecutor

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/teamspace/uploads/fannilla-cfd25ffd1b7c.json"

BUCKET_NAME = 'chum_bucket_stuff'
CLIENT = storage.Client()

BUCKET = CLIENT.bucket(BUCKET_NAME)
DESTINATION_FOLDER = Path("/Volumes/external_drive")

CATEGORIES = [
    'amateur', 'asian', 'ass', 'babe', 'bath', 'beautiful', 'big-tits', 'bikini', 'blonde', 'bondage', 'boots',
    'brazilian', 'brunette', 'centerfold', 'christmas', 'chubby', 'clothed', 'college', 'cosplay', 'cougar', 'curvy',
    'doggystyle', 'ebony', 'european', 'face', 'fake-tits', 'feet', 'girlfriend', 'glamour', 'glasses', 'granny',
    'hairy', 'high-heels', 'homemade', 'housewife', 'japanese', 'jeans', 'latex', 'latina', 'legs', 'lingerie', 'maid',
    'masturbation', 'mature', 'milf', 'model', 'mom', 'natural-tits', 'nipples', 'non-nude', 'nurse', 'office',
    'oiled', 'panties', 'pantyhose', 'pool', 'pornstar', 'redhead', 'saggy-tits', 'secretary', 'selfie', 'sexy',
    'shaved', 'short-hair', 'shorts', 'skinny', 'skirt', 'smoking', 'socks', 'solo', 'sports', 'spreading', 'stockings',
    'tattoo', 'teen', 'thai', 'thick', 'thong', 'undressing', 'uniform', 'upskirt', 'white', 'yoga-pants'
]


def fetch_all_blobs(folder_prefix: str) -> List[str]:
    """Fetch all file paths from the GCS bucket."""
    _blobs = BUCKET.list_blobs(prefix=f"pics/{folder_prefix}")
    return [blob.name for blob in _blobs]


def download_blob(blob_name: str, force_download: bool, pbar: tqdm) -> None:
    """Download a blob from the GCS bucket."""
    file_path = DESTINATION_FOLDER / blob_name.replace("pics/", "")

    file_path.parent.mkdir(parents=True, exist_ok=True)
    if not force_download and file_path.exists():
        pbar.update(1)
        return

    BUCKET.blob(blob_name).download_to_filename(file_path.as_posix())
    pbar.update(1)


async def download_category(category_blobs: List[str], force_download: bool) -> None:
    loop = asyncio.get_running_loop()

    with tqdm(total=len(category_blobs), desc=f"Category {category_blobs[0].split('/')[1]}") as pbar:
        with ThreadPoolExecutor() as executor:
            tasks = [
                loop.run_in_executor(executor, download_blob, blob_name, force_download, pbar)
                for blob_name in category_blobs
            ]
            await asyncio.gather(*tasks)


if __name__ == "__main__":
    for category in CATEGORIES:
        blobs = fetch_all_blobs(category)
        asyncio.run(download_category(blobs, force_download=False))
