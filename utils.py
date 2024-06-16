import os
import shutil
from pathlib import Path
from google.cloud import vision
from google.cloud import storage

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = f"{os.getcwd()}/fannilla-dev.json"

vision_client = vision.ImageAnnotatorClient()
storage_client = storage.Client()

BUCKET_NAME = 'chum_bucket_stuff'
_path = Path("/Volumes/external_drive/fannilla")

if _path.is_dir():
    SRC_DIR = _path  # Local SSD
elif 'workspace/' in str(os.getcwd()):
    SRC_DIR = Path("/workspace/images")  # Runpod
elif 'teamspace/studios/this_studio/' in str(os.getcwd()):
    SRC_DIR = Path("/teamspace/studios/this_studio/images")  # Lightning ai
else:
    SRC_DIR = Path("./images")  # Other

BUCKET = storage_client.bucket(BUCKET_NAME)


class MultiPath:
    def __init__(self, structure_path: str):
        self.local_path: Path = SRC_DIR / structure_path
        self.gcp_location: str = f"pics/{structure_path}"

    def copy_to_gcp(self, force: bool = False):
        def _save_to_gcp():
            BUCKET.blob(self.gcp_location).upload_from_filename(self.local_path.as_posix())

        if force:
            _save_to_gcp()
            return True
        else:
            if BUCKET.blob(self.gcp_location).exists():
                return False
            _save_to_gcp()

    def copy_from_gcp(self, force: bool = False):
        if force:
            BUCKET.blob(self.gcp_location).download_to_filename(self.local_path.as_posix())
            return True
        else:
            if self.local_path.exists():
                return False
            self.local_path.parent.mkdir(parents=True, exist_ok=True)


