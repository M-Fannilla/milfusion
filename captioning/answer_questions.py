from pathlib import Path

import torch
import pandas as pd
from PIL import Image
from tqdm import tqdm
from questions import Questions
from model import moondream, moondream_tokenizer
from utils import IMG_DIR, ANSWER_DIR, QUESTIONS_DIR, CAPTION_DIR

BATCH_SIZE = 8

IMG_DIR.mkdir(exist_ok=True)
ANSWER_DIR.mkdir(exist_ok=True)
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
    questions = [str(question.value) for question in Questions]
    print("Processing file:", filename)

    all_ans = []
    for i in range(0, len(questions), BATCH_SIZE):
        batch_questions = questions[i:i + BATCH_SIZE]
        batch_question_answers = moondream.batch_answer(
            images=[img] * len(batch_questions),
            prompts=batch_questions,
            tokenizer=moondream_tokenizer,
        )
        all_ans.extend(batch_question_answers)

    out = dict(zip(questions, all_ans))
    filename = Path(filename).with_suffix(".json")
    out_path = QUESTIONS_DIR / filename
    out_path.write_text(str(out))
    print("\tSaved answers to:", out_path)


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

    for filename in tqdm(filenames):
        process_questions(filename)

    print("Processing complete and CSV file saved.")
