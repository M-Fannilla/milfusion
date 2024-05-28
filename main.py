import os
from PIL import Image
import gradio as gr


# Function to get categories
def get_categories():
    return [d for d in os.listdir('images') if os.path.isdir(os.path.join('images', d))]


# Function to get galleries within a category
def get_galleries(category):
    return [d for d in os.listdir(os.path.join('images', category)) if
            os.path.isdir(os.path.join('images', category, d))]


# Function to get images within a gallery
def get_images(category, gallery):
    path = os.path.join('images', category, gallery)
    images = [f for f in os.listdir(path) if os.path.isfile(os.path.join(path, f))]
    vertical_images = [img for img in images if
                       Image.open(os.path.join(path, img)).height > Image.open(os.path.join(path, img)).width]
    horizontal_images = [img for img in images if
                         Image.open(os.path.join(path, img)).width >= Image.open(os.path.join(path, img)).height]
    return vertical_images, horizontal_images


# Function to load and display images
def load_images(category, gallery):
    vertical_images, horizontal_images = get_images(category, gallery)
    if vertical_images:
        vertical_image = Image.open(os.path.join('images', category, gallery, vertical_images[0]))
    else:
        vertical_image = None
    if horizontal_images:
        horizontal_image = Image.open(os.path.join('images', category, gallery, horizontal_images[0]))
    else:
        horizontal_image = None
    return vertical_image, horizontal_image


# Function to crop and save images
def crop_and_save_images(category, gallery, vertical_crop, horizontal_crop):
    vertical_images, horizontal_images = get_images(category, gallery)

    for img in vertical_images:
        image_path = os.path.join('images', category, gallery, img)
        image = Image.open(image_path)
        cropped_image = image.crop(
            (vertical_crop['left'], vertical_crop['top'], vertical_crop['right'], vertical_crop['bottom']))
        cropped_image.save(image_path)

    for img in horizontal_images:
        image_path = os.path.join('images', category, gallery, img)
        image = Image.open(image_path)
        cropped_image = image.crop(
            (horizontal_crop['left'], horizontal_crop['top'], horizontal_crop['right'], horizontal_crop['bottom']))
        cropped_image.save(image_path)

    return f"Cropped images saved in {os.path.join('images', category, gallery)}"


# Gradio app layout
with gr.Blocks() as app:
    category = gr.Dropdown(label="Category", choices=get_categories(), value=get_categories()[0])
    gallery = gr.Dropdown(label="Gallery")
    category.change(lambda x: gr.update(choices=get_galleries(x), value=get_galleries(x)[0]), inputs=category,
                    outputs=gallery)

    vertical_image = gr.Image(type="pil")
    horizontal_image = gr.Image(type="pil")
    gallery.change(lambda cat, gal: load_images(cat, gal), inputs=[category, gallery],
                   outputs=[vertical_image, horizontal_image])

    vertical_crop = gr.Image(type="numpy", tool="select", label="Vertical Image Crop")
    horizontal_crop = gr.Image(type="numpy", tool="select", label="Horizontal Image Crop")

    crop_button = gr.Button("Crop and Save")
    crop_button.click(crop_and_save_images, inputs=[category, gallery, vertical_crop, horizontal_crop],
                      outputs=gr.Textbox())

# Run the app
app.launch()