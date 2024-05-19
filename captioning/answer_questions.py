import torch
import pandas as pd
from PIL import Image
from tqdm import tqdm
from transformers import AutoTokenizer, AutoModelForCausalLM

from captioning.questions import Questions
from utils import IMG_DIR, ANSWER_DIR, QUESTIONS_DIR

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
    questions = [question.value for question in Questions]

    batch_question_answers = model.batch_answer(
        images=[img] * len(questions),
        prompts=questions,
        tokenizer=tokenizer,
    )

    out = {q: ans for q, ans in zip(questions, batch_question_answers)}

    out_path = ANSWER_DIR / f"{filename}.json"
    out_path.write_text(str(out))


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


if __name__ == "__main__":
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

    for filename in tqdm(filenames):
        process_questions(filename)

    print("Processing complete and CSV file saved.")
