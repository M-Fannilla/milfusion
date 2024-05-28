import os
from tqdm import tqdm
import concurrent.futures
from google.cloud import storage

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = "/teamspace/uploads/fannilla-cfd25ffd1b7c.json"

def fetch_all_blobs(bucket_name, folder_prefix):
    """Fetch all file paths from the GCS bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blobs = bucket.list_blobs(prefix=folder_prefix)
    return [blob.name for blob in blobs]

def download_blob(bucket_name, blob_name, destination_folder, force_download, progress_bar):
    """Download a blob from the GCS bucket."""
    storage_client = storage.Client()
    bucket = storage_client.bucket(bucket_name)
    blob = bucket.blob(blob_name)
    
    local_path = os.path.join(destination_folder, blob_name)
    os.makedirs(os.path.dirname(local_path), exist_ok=True)
    
    if not os.path.exists(local_path) or force_download:
        blob.download_to_filename(local_path)
        progress_bar.set_description(f"Downloaded {blob_name}")
    else:
        progress_bar.set_description(f"Skipped {blob_name}, file already exists")

    progress_bar.update(1)

def download_bucket(bucket_name, destination_folder, folder_prefix,force_download=False):
    """Download the entire GCS bucket to the local folder."""
    blobs = fetch_all_blobs(bucket_name, folder_prefix)
    print(f"Found {len(blobs)} files in the bucket {bucket_name}")
    
    with tqdm(total=len(blobs), desc="Downloading files") as progress_bar:
        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [
                executor.submit(download_blob, bucket_name, blob_name, destination_folder, force_download, progress_bar)
                for blob_name in blobs
            ]
            for future in concurrent.futures.as_completed(futures):
                try:
                    future.result()
                except Exception as e:
                    print(f"Error downloading file: {e}")
                    progress_bar.update(1)

if __name__ == "__main__":
    gcp = [
        'amateur', 'bath', 'big-tits', 'bikini', 'blonde', 'boots', 'brunette', 'centerfold', 'christmas', 'chubby', 
        'clothed', 'cougar', 'curvy', 'doggystyle', 'face', 'fake-tits', 'feet', 'glasses', 'granny',
        'hairy', 'high-heels', 'homemade', 'housewife', 'jeans', 'legs', 'lingerie', 'maid', 'masturbation', 'mature', 
        'milf', 'model', 'mom', 'natural-tits', 'non-nude', 'nude', 'nurse', 'office', 'panties', 'pantyhose', 'pool', 
        'pornstar', 'redhead', 'saggy-tits', 'secretary', 'selfie', 
        'sexy', 'shaved', 'short-hair', 'shorts', 'skinny', 
        'skirt', 'smoking', 'socks', 'solo', 'spreading', 'stockings', 'thick', 'thong', 'undressing', 'upskirt', 'white'
    ]

    BUCKET_NAME = 'pornpics_scrape'

    for prefix in gcp:
        DESTINATION_FOLDER = f"images/{prefix}"
        if not os.path.exists(DESTINATION_FOLDER):
            os.makedirs(DESTINATION_FOLDER)

        download_bucket(BUCKET_NAME, DESTINATION_FOLDER, prefix, False)
