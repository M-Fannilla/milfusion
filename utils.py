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

try:
    (_path / '_').mkdir(exist_ok=True, parents=True)
    shutil.rmtree(_path / '_')
    SRC_DIR = _path
except PermissionError as e:
    SRC_DIR = Path("./images")

BUCKET = storage_client.bucket(BUCKET_NAME)
