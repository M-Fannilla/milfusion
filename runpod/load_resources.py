import torch
from transformers import AutoModelForCausalLM, AutoTokenizer, BitsAndBytesConfig

MODEL_PATH = "THUDM/cogvlm2-llama3-chat-19B"
DEVICE = 'cuda' if torch.cuda.is_available() else 'cpu'

cuda_available = torch.cuda.is_available()
capability = torch.cuda.get_device_capability()[0]

TORCH_TYPE = torch.bfloat16 if cuda_available and capability >= 8 else torch.float16
NUM_GPU = torch.cuda.device_count()


def get_tokenizer_and_model(quant: int | None = None):
    tokenizer = AutoTokenizer.from_pretrained(
        MODEL_PATH, trust_remote_code=True
    )

    if quant:
        bb_config = (
            BitsAndBytesConfig(load_in_4bit=True) if quant == 4
            else BitsAndBytesConfig(load_in_8bit=True)
        )

        model = AutoModelForCausalLM.from_pretrained(
            MODEL_PATH,
            torch_dtype=TORCH_TYPE,
            trust_remote_code=True,
            quantization_config=bb_config,
            low_cpu_mem_usage=True
        )

    else:
        model = AutoModelForCausalLM.from_pretrained(
            MODEL_PATH,
            torch_dtype=TORCH_TYPE,
            trust_remote_code=True
        ).to(DEVICE)

    model = model.eval()

    return tokenizer, model
