import pandas as pd
from PIL import Image
from tqdm import tqdm
from pathlib import Path
from model import moondream, moondream_tokenizer

from utils import IMG_DIR, ANSWER_DIR, CAPTION_DIR

BATCH_SIZE = 8

IMG_DIR.mkdir(exist_ok=True)
ANSWER_DIR.mkdir(exist_ok=True)

prompt_short = "Describe the image."
prompt_long = "Provide a detailed description of the image, including key elements like colors, textures, and the composition of objects. This description will be used to train generative AI, enhancing its ability to recognize and replicate similar visuals accurately."


def process_images(batch_filenames: list[str]):
    batch_images = [
        Image.open((IMG_DIR / filename).as_posix()).convert("RGB")
        for filename in batch_filenames
    ]
    batch_answers = moondream.batch_answer(
        images=batch_images,
        prompts=[prompt_long] * len(batch_filenames),
        tokenizer=moondream_tokenizer,
    )
    save_description_batch(batch_filenames, batch_answers)


def save_description_batch(filenames: list[str], descriptions: list[str]):
    for filename, description in zip(filenames, descriptions):
        with open(ANSWER_DIR / Path(filename).with_suffix('.txt'), 'w') as file:
            file.write(description)


if __name__ == "__main__":
    df = pd.read_csv(CAPTION_DIR / "image_resolutions.csv")

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
            batch_filenames=filenames[i:i + BATCH_SIZE]
        )

    print("Processing complete and CSV file saved.")
