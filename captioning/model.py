import torch
from transformers import AutoTokenizer, AutoModelForCausalLM

revision = "2024-05-08"
model_id = "vikhyatk/moondream2"


def detect_device():
    if torch.cuda.is_available():
        return torch.device("cuda"), torch.float16
    else:
        return torch.device("cpu"), torch.float32


device, dtype = detect_device()
print("Using device:", device)

moondream_tokenizer = AutoTokenizer.from_pretrained(model_id, revision=revision, force_download=True)
print("Tokenizer loaded successfully")

moondream = AutoModelForCausalLM.from_pretrained(
    model_id, trust_remote_code=True, revision=revision,
    torch_dtype=dtype,
    attn_implementation="flash_attention_2",
    force_download=True
)
moondream.to(device=device)

print("Model loaded successfully")
moondream.eval()
print("Setting model in evaluation mode")
