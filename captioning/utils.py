import platform
from pathlib import Path
import os

if platform.platform().startswith("macOS"):
    IMG_DIR = Path("./images")
    CAPTION_DIR = Path("./captioning")
else:
    IMG_DIR = Path("/teamspace/uploads")
    CAPTION_DIR = Path("/teamspace/studios/this_studio/milfusion/captioning")
    
ANSWER_DIR = CAPTION_DIR / "_desc"
QUESTIONS_DIR = CAPTION_DIR / "_questions" 
