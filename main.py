import os
from pathlib import Path

import gradio as gr
import pandas as pd
from PIL import Image

from captioning.utils import CAPTION_DIR, IMG_DIR

# Load data from CSV
data = pd.read_csv('image_data.csv')


def update_image_properties(index, **properties):
    # Update the DataFrame with new values
    for key, value in properties.items():
        data.at[index, key] = value
    data.at[index, 'status'] = "reviewed"
    return "Properties Updated!"


def show_images(image_index):
    image_path = data.iloc[image_index]['filename']

    for true_filename in os.listdir(IMG_DIR):
        if Path(true_filename).stem.lower() == image_path:
            image_path = true_filename
            break

    image = Image.open(IMG_DIR / image_path)

    properties = {col: data.iloc[image_index][col] for col in data.columns if col not in ['filename']}

    # Return image and dynamic properties
    return [image] + list(properties.values())


# Gradio interface
with gr.Blocks() as demo:
    with gr.Row():
        with gr.Column():
            outputs = [gr.Image()]
            image_index = gr.Dropdown(label="Select Image", choices=list(range(len(data))))
            inputs = [image_index]

        with gr.Column():
            property_widgets = {}

            data_cols = list(data.columns)
            data_cols.remove('filename')

            for col in data_cols:
                if col == 'status':
                    widget = gr.Checkbox
                else:
                    widget = gr.Textbox

                property_widgets[col] = widget(label=col)
                outputs.append(property_widgets[col])
                inputs.append(property_widgets[col])

            update_button = gr.Button("Update Properties")
            update_button.click(
                fn=update_image_properties,
                inputs=inputs,
                outputs=gr.Textbox()
            )

            image_index.change(fn=show_images, inputs=image_index, outputs=outputs)

demo.launch()
