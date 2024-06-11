import torch
from transformers import AutoModel, AutoTokenizer, AutoModelForCausalLM

ckpt_path = "internlm/internlm-xcomposer2-vl-7b"
# ckpt_path = 'internlm/internlm-xcomposer2-4khd-7b'

tokenizer = AutoTokenizer.from_pretrained(
    ckpt_path, trust_remote_code=True
).cuda()

model = AutoModelForCausalLM.from_pretrained(
    ckpt_path, torch_dtype=torch.float16, trust_remote_code=True
).cuda()

model = model.eval()
torch.set_grad_enabled(False)


def composer(image_path: str, prompt: str) -> str:
    query = f'<ImageHere>{prompt}'
    image = image_path
    with torch.cuda.amp.autocast():
        response, _ = model.chat(
            tokenizer, query=query, image=image, history=[], do_sample=False
        )
    return str(response)
