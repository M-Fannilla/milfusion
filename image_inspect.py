import os
from PIL import Image
import pandas as pd


def fetch_and_plot_image_resolutions_from_directory(directory_path):
    """
    Reads images from the specified directory, stores their dimensions,
    and plots the distribution of image resolutions.

    :param directory_path: Path to the directory containing images
    """
    # List to store image dimensions
    image_dimensions = []

    # List all files in the directory
    for filename in os.listdir(directory_path):
        if filename.lower().endswith(('.png', '.jpg', '.jpeg', '.bmp', '.gif', '.tiff')):
            file_path = os.path.join(directory_path, filename)
            try:
                image = Image.open(file_path)
                width, height = image.size
                image_dimensions.append((filename, width, height))
            except Exception as e:
                print(f"Could not process image {file_path}: {e}")

    # Create a DataFrame with the dimensions
    df = pd.DataFrame(image_dimensions, columns=['filename', 'width', 'height'])
    df.to_csv("image_resolutions.csv", index=False)


if __name__ == "__main__":
    directory_path = 'images'  # Replace with the actual path to your directory
    fetch_and_plot_image_resolutions_from_directory(directory_path)
