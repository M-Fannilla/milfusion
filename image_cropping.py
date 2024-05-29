import concurrent.futures
from pathlib import Path
from PIL import Image

SRC_DIR = Path("images")


def open_and_crop_image(image_path):
    """Open an image, crop it symmetrically by 10%, and save the cropped image."""
    try:
        image = Image.open(image_path)
        width, height = image.size

        # Calculate the crop dimensions (10% from each side)
        left = width * 0.1
        upper = height * 0.1
        right = width * 0.9
        lower = height * 0.9

        # Crop and save the image
        cropped_image = image.crop((left, upper, right, lower))
        cropped_image.save(image_path)

        return image_path, cropped_image
    except Exception as e:
        return image_path, str(e)


def crop_images_in_gallery(gallery_path):
    """Open and crop all images in the specified gallery."""
    image_paths = list(gallery_path.glob("*.jpg"))  # Adjust the glob pattern as needed

    with concurrent.futures.ThreadPoolExecutor() as executor:
        results = list(executor.map(open_and_crop_image, image_paths))

    return results


def process_category(category):
    """Process all galleries within a specified category."""
    category_path = SRC_DIR / category
    galleries = [d for d in category_path.iterdir() if d.is_dir()]

    all_results = {}
    for gallery in galleries:
        try:
            all_results[gallery] = crop_images_in_gallery(gallery)
            print(f"Processed gallery {gallery}")
        except Exception as e:
            print(f"Failed to process gallery {gallery}: {e}")

    return all_results


if __name__ == "__main__":
    # Example usage
    category = "mature"
    results = process_category(category)

    # Print results
    for gallery, cropped_results in results.items():
        for image_path, result in cropped_results:
            if isinstance(result, str):
                print(f"  Failed to process {image_path}: {result}")
            else:
                print(f"  Successfully processed {image_path}")