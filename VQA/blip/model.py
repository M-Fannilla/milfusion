import torch
from PIL import Image
from transformers import BlipProcessor, BlipForQuestionAnswering

model_name = "ybelkada/blip-vqa-capfilt-large"
processor = BlipProcessor.from_pretrained(model_name)
model = BlipForQuestionAnswering.from_pretrained(
    model_name, torch_dtype=torch.float16
).to("cuda")


def blip(image_path: str, prompt: str):
    raw_image = Image.open(image_path).convert('RGB')
    inputs = processor(raw_image, prompt, return_tensors="pt").to("cuda", torch.float16)
    out = model.generate(**inputs)
    print(processor.decode(out[0], skip_special_tokens=True))
