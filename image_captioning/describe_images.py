import torch
from tqdm import tqdm
import pandas as pd
from PIL import Image
from pathlib import Path
from concurrent.futures import ThreadPoolExecutor
from transformers import AutoTokenizer, AutoModelForCausalLM

BATCH_SIZE = 8

IMG_DIR = Path("./images")
ANSWER_DIR = Path("./image_descriptions_att")

IMG_DIR.mkdir(exist_ok=True)
ANSWER_DIR.mkdir(exist_ok=True)

revision = "2024-05-08"
model_id = "vikhyatk/moondream2"


def detect_device():
    if torch.cuda.is_available():
        return torch.device("cuda"), torch.float16
    else:
        return torch.device("cpu"), torch.float32


def write_answer(file_name, answer):
    with (ANSWER_DIR / file_name).open("w") as f:
        f.write(answer)


if __name__ == "__main__":
    device, dtype = detect_device()
    print("Using device:", device)

    tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision)
    print("Tokenizer loaded successfully")

    model = AutoModelForCausalLM.from_pretrained(
        model_id, trust_remote_code=True, revision=revision,
        torch_dtype=torch.float16, attn_implementation="flash_attention_2"
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

    filenames = df['filename'].to_list()  # Corrected method to get filenames
    print("Starting to process images...")

    with ThreadPoolExecutor() as executor:
        for i in tqdm(range(0, len(filenames), BATCH_SIZE)):
            batch_filenames = filenames[i:i + BATCH_SIZE]
            images = [
                Image.open((IMG_DIR / file_name).as_posix()).convert("RGB")
                for file_name in batch_filenames
            ]
            answers = model.batch_answer(
                images=images,
                prompts=["Describe this picture."] * len(batch_filenames),
                tokenizer=tokenizer,
            )

            for file_name, answer in zip(batch_filenames, answers):
                file_name = file_name.lower()

                if file_name.endswith(".jpeg"):
                    file_name = file_name.replace(".jpeg", ".txt")
                elif file_name.endswith(".jpg"):
                    file_name = file_name.replace(".jpg", ".txt")
                elif file_name.endswith(".png"):
                    file_name = file_name.replace(".png", ".txt")
                else:
                    file_name = file_name + ".txt"

                file_name = file_name.replace(".jpg", ".txt")
                executor.submit(write_answer, file_name, answer)
