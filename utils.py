import platform
from pathlib import Path

if platform.platform().startswith("macOS"):
    IMG_DIR = Path("./images")
    ANSWER_DIR = Path("./captioning/_desc")
else:
    IMG_DIR = Path("./teamspace/uploads")
    ANSWER_DIR = Path("./milfusion/captioning/_desc")
