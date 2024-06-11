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

if 'workspace/' in str(os.getcwd()):
    SRC_DIR = Path("/workspace/images")
else:
    if _path.is_dir():
        SRC_DIR = _path
    else:
        SRC_DIR = Path("./images")
BUCKET = storage_client.bucket(BUCKET_NAME)
