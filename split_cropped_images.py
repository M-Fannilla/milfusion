import os
import shutil
import random


def split_dataset(input_folder, output_folder, train_ratio=0.8):
    # Create the output directories if they do not exist
    train_folder = os.path.join(output_folder, 'train')
    validation_folder = os.path.join(output_folder, 'validation')
    os.makedirs(train_folder, exist_ok=True)
    os.makedirs(validation_folder, exist_ok=True)

    # Get a list of all files in the input folder
    all_files = [
        f for f in os.listdir(input_folder)
        if os.path.isfile(os.path.join(input_folder, f)) and f.endswith('.jpg')
    ]

    # Shuffle the files
    random.shuffle(all_files)

    # Split the files into training and validation sets
    train_files = all_files[:int(len(all_files) * train_ratio)]
    validation_files = all_files[int(len(all_files) * train_ratio):]

    # Move the files to their respective directories
    for file in train_files:
        shutil.move(os.path.join(input_folder, file), os.path.join(train_folder, file))

    for file in validation_files:
        shutil.move(os.path.join(input_folder, file), os.path.join(validation_folder, file))

    print(f"Total files: {len(all_files)}")
    print(f"Training files: {len(train_files)}")
    print(f"Validation files: {len(validation_files)}")


if __name__ == "__main__":
    source_folder = 'cropped_images'
    target_folder = 'sexy_images'
    split_dataset(source_folder, target_folder, train_ratio=0.8)
