import json

import torch
import pandas as pd
from PIL import Image
from tqdm import tqdm
from pathlib import Path
from questions import ImageQuestions
from model import moondream, moondream_tokenizer
from utils import IMG_DIR, ANSWER_DIR, QUESTIONS_DIR, CAPTION_DIR

BATCH_SIZE = 8

# IMG_DIR.mkdir(exist_ok=True)
# ANSWER_DIR.mkdir(exist_ok=True)
QUESTIONS_DIR.mkdir(exist_ok=True)

revision = "2024-05-08"
model_id = "vikhyatk/moondream2"


def detect_device():
    if torch.cuda.is_available():
        return torch.device("cuda"), torch.float16
    else:
        return torch.device("cpu"), torch.float32


def process_questions(filename: str):
    img = Image.open((IMG_DIR / filename).as_posix()).convert("RGB")
    questions = [str(question.value) for question in ImageQuestions]

    all_ans = []
    for i in range(0, len(questions), BATCH_SIZE):
        batch_questions = questions[i:i + BATCH_SIZE]
        batch_question_answers = moondream.batch_answer(
            images=[img] * len(batch_questions),
            prompts=batch_questions,
            tokenizer=moondream_tokenizer,
        )
        all_ans.extend(batch_question_answers)

    data = dict(zip([str(question.name) for question in ImageQuestions], all_ans))
    filename = Path(filename).with_suffix(".json")
    out_path = QUESTIONS_DIR / filename

    with open(out_path, 'w') as f:
        json.dump(data, f)


if __name__ == "__main__":
    df = pd.read_csv(CAPTION_DIR / "image_resolutions.csv")

    min_width = 512
    min_height = 512

    df = df[
        (df.width > min_width)
        & (df.height > min_height)
        # & (df.width < max_width)
        # & (df.height < max_height)
        ]

    filenames = df['filename'].to_list()

    print("Starting to process images...")

    for i, filename in enumerate(filenames):
        _name_check = Path(filename).with_suffix(".json")
        if (QUESTIONS_DIR / Path(filename).with_suffix(".json")).exists():
            print(f"Image {filename} already processed.")
        else:
            print(f"Processing {i}/{len(filenames)}: {filename}")
            process_questions(filename)
            print()

    print("Processing complete and CSV file saved.")
