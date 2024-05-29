import os
from pathlib import Path
from PIL import Image
import gradio as gr

SRC_DIR = Path('images')


def get_categories():
    return [
        d
        for d in os.listdir(SRC_DIR)
        if (SRC_DIR / d).is_dir()
    ]


def get_galleries(cat: str):
    return [
        d for d in os.listdir(SRC_DIR / cat)
        if os.path.isdir(SRC_DIR / cat / d)
    ]


def get_images(category, gallery):
    path = SRC_DIR / category / gallery

    images = [
        f for f in os.listdir(path)
        if (path / f).is_file() and not (path / f).as_posix().endswith(".txt")
    ]

    vertical_images = [
        img for img in images if
        Image.open(os.path.join(path, img)).height > Image.open(os.path.join(path, img)).width
    ]

    horizontal_images = [
        img for img in images if
        Image.open(os.path.join(path, img)).width >= Image.open(os.path.join(path, img)).height
    ]

    return vertical_images, horizontal_images


def load_images(category, gallery):
    vertical_images, horizontal_images = get_images(category, gallery)
    if vertical_images:
        vertical_image = Image.open((SRC_DIR / category / gallery / vertical_images[0]).as_posix())
    else:
        vertical_image = None
    if horizontal_images:
        horizontal_image = Image.open((SRC_DIR / category / gallery / horizontal_images[0]).as_posix())
    else:
        horizontal_image = None
    return vertical_image, horizontal_image


def crop_and_save_images_from_top_left(
        category, gallery, vertical_image_editor, horizontal_image_editor
):
    vertical_images, horizontal_images = get_images(category, gallery)
    curr_vertical, curr_horizontal = load_images(category, gallery)

    if vertical_images:
        cropped_vertical_width = vertical_image_editor['composite'].shape[1]
        cropped_vertical_height = vertical_image_editor['composite'].shape[0]
        curr_vertical_width, curr_vertical_height = curr_vertical.size

        # calculate percentage of crop for vertical image
        vertical_width_ratio = cropped_vertical_width / curr_vertical_width
        vertical_height_ratio = cropped_vertical_height / curr_vertical_height

        for img in vertical_images:
            image_path = SRC_DIR / category / gallery / img
            image = Image.open(image_path)
            width, height = image.size
            right = int(width * vertical_width_ratio)
            bottom = int(height * vertical_height_ratio)
            cropped_image = image.crop((0, 0, right, bottom))
            cropped_image.save(image_path)

    if horizontal_images:
        cropped_horizontal_width = horizontal_image_editor['composite'].shape[1]
        cropped_horizontal_height = horizontal_image_editor['composite'].shape[0]
        curr_horizontal_width, curr_horizontal_height = curr_horizontal.size

        # calculate percentage of crop for horizontal image
        horizontal_width_ratio = round(cropped_horizontal_width / curr_horizontal_width, 2)
        horizontal_height_ratio = round(cropped_horizontal_height / curr_horizontal_height, 2)

        for img in horizontal_images:
            image_path = SRC_DIR / category / gallery / img
            image = Image.open(image_path)
            width, height = image.size
            right = int(width * horizontal_width_ratio)
            bottom = int(height * horizontal_height_ratio)
            cropped_image = image.crop((0, 0, right, bottom))
            cropped_image.save(image_path)

    return f"Cropped images saved in {os.path.join('images', category, gallery)}"

def crop_and_save_images_from_bottom_right(
        category, gallery, vertical_image_editor, horizontal_image_editor
):
    vertical_images, horizontal_images = get_images(category, gallery)
    curr_vertical, curr_horizontal = load_images(category, gallery)

    if vertical_images:
        cropped_vertical_width = vertical_image_editor['composite'].shape[1]
        cropped_vertical_height = vertical_image_editor['composite'].shape[0]
        curr_vertical_width, curr_vertical_height = curr_vertical.size

        # calculate percentage of crop for vertical image
        vertical_width_ratio = cropped_vertical_width / curr_vertical_width
        vertical_height_ratio = cropped_vertical_height / curr_vertical_height

        for img in vertical_images:
            image_path = SRC_DIR / category / gallery / img
            image = Image.open(image_path)
            width, height = image.size
            left = int(width - (width * vertical_width_ratio))
            upper = int(height - (height * vertical_height_ratio))
            cropped_image = image.crop((left, upper, width, height))
            cropped_image.save(image_path)

    if horizontal_images:
        cropped_horizontal_width = horizontal_image_editor['composite'].shape[1]
        cropped_horizontal_height = horizontal_image_editor['composite'].shape[0]
        curr_horizontal_width, curr_horizontal_height = curr_horizontal.size

        # calculate percentage of crop for horizontal image
        horizontal_width_ratio = round(cropped_horizontal_width / curr_horizontal_width, 2)
        horizontal_height_ratio = round(cropped_horizontal_height / curr_horizontal_height, 2)

        for img in horizontal_images:
            image_path = SRC_DIR / category / gallery / img
            image = Image.open(image_path)
            width, height = image.size
            left = int(width - (width * horizontal_width_ratio))
            upper = int(height - (height * horizontal_height_ratio))
            cropped_image = image.crop((left, upper, width, height))
            cropped_image.save(image_path)

    return f"Cropped images saved in {os.path.join('images', category, gallery)}"


# Gradio app layout
with gr.Blocks() as app:
    category = gr.Dropdown(label="Category", choices=get_categories(), value=get_categories()[0])
    gallery = gr.Dropdown(label="Gallery")
    category.change(
        lambda x: gr.update(choices=get_galleries(x), value=get_galleries(x)[0]), inputs=category,
        outputs=gallery
    )

    with gr.Row():
        with gr.Column():
            vertical_image_editor = gr.ImageEditor(label="Vertical Image Editor")
        with gr.Column():
            horizontal_image_editor = gr.ImageEditor(label="Horizontal Image Editor")

    gallery.change(
        lambda cat, gal: load_images(cat, gal),
        inputs=[category, gallery],
        outputs=[vertical_image_editor, horizontal_image_editor]
    )
    with gr.Row():
        crop_br_button = gr.Button("Bottom Right Crop")
        crop_br_button.click(
            crop_and_save_images_from_bottom_right,
            inputs=[
                category, gallery,
                vertical_image_editor,
                horizontal_image_editor
            ],
            outputs=gr.Textbox()
        )
        crop_tl_button = gr.Button("Top Left Crop")
        crop_tl_button.click(
            crop_and_save_images_from_top_left,
            inputs=[
                category, gallery,
                vertical_image_editor,
                horizontal_image_editor
            ],
            outputs=gr.Textbox()
        )

app.launch()

# if __name__ == "__main__":
# imgs = get_images('mature', "all-over-30-alana-luv-95575580")
# print(imgs)

# wifey-artemesia-loses-purple-lingerie-and-rides-her-mature-hairy-cunt-on-toy-38278000
