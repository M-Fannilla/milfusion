import torch
from PIL import Image

from transformers import AutoModel, AutoTokenizer

# model_name = 'openbmb/MiniCPM-Llama3-V-2_5'
model_name = 'openbmb/MiniCPM-Llama3-V-2_5-int4'

model = AutoModel.from_pretrained(model_name, trust_remote_code=True, torch_dtype=torch.float16)
model = model.to(device='cuda')

tokenizer = AutoTokenizer.from_pretrained(model_name, trust_remote_code=True)
model.eval()


def minicpm_llama(image_path: str, prompt: str) -> list[str]:
    res = model.chat(
        image=Image.open(image_path).convert('RGB'),
        msgs=[{'role': 'user', 'content': prompt}],
        tokenizer=tokenizer,
        sampling=True,  # if sampling=False, beam_search will be used by default
        temperature=0.5,
    )
    return res
# 1. Check fot beam_search vs sampling
# 2. Check for streaming
