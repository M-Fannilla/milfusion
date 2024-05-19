import torch
from tqdm import tqdm
import pandas as pd
from PIL import Image
from pathlib import Path
from model import moondream, moondream_tokenizer

from utils import IMG_DIR, ANSWER_DIR, CAPTION_DIR

BATCH_SIZE = 8

IMG_DIR.mkdir(exist_ok=True)
ANSWER_DIR.mkdir(exist_ok=True)


def process_images(batch_descriptions: list[str]):
    batch_answers = moondream.batch_answer(
        prompts=["Process this prompt to make it ideal for stable generative ai"] * len(batch_descriptions),
        tokenizer=moondream_tokenizer,
    )
    save_description_batch(batch_filenames, batch_answers)


def save_description_batch(filenames: list[str], descriptions: list[str]):
    for filename, description in zip(filenames, descriptions):
        with open(ANSWER_DIR / Path(filename).with_suffix('_refine.txt'), 'w') as file:
            file.write(description)


if __name__ == "__main__":
    df = pd.read_csv(CAPTION_DIR / "filenames_with_descriptions.csv")

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
        process_images(
            batch_filenames=filenames[i:i + BATCH_SIZE],
            model=moondream,
            tokenizer=moondream_tokenizer
        )

    print("Processing complete and CSV file saved.")
