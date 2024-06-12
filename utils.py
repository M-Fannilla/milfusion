import os
import shutil
from pathlib import Path
from google.cloud import vision
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "fannilla-dev.json"

vision_client = vision.ImageAnnotatorClient()
storage_client = storage.Client()

BUCKET_NAME = 'chum_bucket_stuff'
_path = Path("/Volumes/external_drive")

if _path.is_dir():
    SRC_DIR = _path  # Local SSD
elif 'workspace/' in str(os.getcwd()):
    SRC_DIR = Path("/workspace/images")  # Runpod
elif 'teamspace/studios/this_studio/' in str(os.getcwd()):
    SRC_DIR = Path("/teamspace/studios/this_studio/images")  # Lightning ai
else:
    SRC_DIR = Path("./images")  # Other

BUCKET = storage_client.bucket(BUCKET_NAME)
