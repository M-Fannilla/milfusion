import os

import pandas as pd
from PIL import Image
from utils import SRC_DIR


def verify_img(img_path):
    try:
        img = Image.open(SRC_DIR / img_path.split("/")[-1])
        img.verify()
        return True
    except Exception as e:
        print(f"Error with {img_path}")
        os.remove(SRC_DIR / img_path.split("/")[-1])
        return False


if __name__ == "__main__":
    df = pd.read_csv(SRC_DIR / "compiled_one_hot.csv", index_col=0)
    original_len = len(df)
    df['good_image'] = df["file_path"].apply(verify_img)
    df = df[df['good_image']]
    new_len = len(df)
    print(f"Removed {original_len - new_len} corrupted images")
    df.to_csv("./datasets/cropped_all_one_hot.csv")
