import torch
from tqdm import tqdm
import pandas as pd
from PIL import Image
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from transformers import AutoTokenizer, AutoModelForCausalLM

BATCH_SIZE = 8

IMG_DIR = Path("/teamspace/uploads")
ANSWER_DIR = Path("./image_descriptions_fa_raw")

IMG_DIR.mkdir(exist_ok=True)
ANSWER_DIR.mkdir(exist_ok=True)

revision = "2024-05-08"
model_id = "vikhyatk/moondream2"


def detect_device():
    if torch.cuda.is_available():
        return torch.device("cuda"), torch.float16
    else:
        return torch.device("cpu"), torch.float32


def process_images(batch_filenames: list[str]):
    batch_images = [
        Image.open((IMG_DIR / filename).as_posix()).convert("RGB")
        for filename in batch_filenames
    ]
    batch_answers = model.batch_answer(
        images=batch_images,
        prompts=["Describe this picture."] * len(batch_filenames),
        tokenizer=tokenizer,
    )
    save_description_batch(batch_filenames, batch_answers)


def save_description_batch(filenames: list[str], descriptions: list[str]):
    for filename, description in zip(filenames, descriptions):
        with open(ANSWER_DIR / Path(filename).with_suffix('.txt'), 'w') as file:
            file.write(description)


if __name__ == "__main__":
    device, dtype = detect_device()
    print("Using device:", device)

    tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)
    print("Tokenizer loaded successfully")

    model = AutoModelForCausalLM.from_pretrained(
        model_id, trust_remote_code=True, revision=revision,
        torch_dtype=dtype, 
        attn_implementation="flash_attention_2"
    ).to(device=device)

    print("Model loaded successfully")
    model.eval()
    print("Setting model in evaluation mode")

    df = pd.read_csv("image_resolutions.csv")

    min_width = 640
    min_height = 640

    df = df[
        (df.width > min_width)
        & (df.height > min_height)
        # & (df.width < max_width)
        # & (df.height < max_height)
        ]

    filenames = df['filename'].to_list()

    print("Starting to process images...")

    total = len(filenames)
    for i in tqdm(range(0, total, BATCH_SIZE)):
        process_images(filenames[i:i + BATCH_SIZE])

    print("Processing complete and CSV file saved.")
