import torch
from PIL import Image
from load_resources import get_tokenizer_and_model, DEVICE, TORCH_TYPE
from runpod.prompts import dynamic_prompt

tokenizer, model = get_tokenizer_and_model(None)

prompt = dynamic_prompt(
    categories=[
        'Caught', 'Cowgirl', 'Cute', 'Reality', 'Hardcore', 'Girlfriend',
        'Amateur', 'Cum In Mouth', 'Russian', 'Big Cock'
    ],
    tags=[
        'Amateur Teen Fuck', 'Teen Sex', 'Teen Hardcore', 'Caught Masturbating',
        'Fuck', 'Amateur Fuck', 'Teen First Time Fuck'
    ]
)

img_path = '/teamspace/studios/this_studio/54465965_090_a6c6.jpg'
image = Image.open(img_path).convert('RGB')

input_by_model = model.build_conversation_input_ids(
    tokenizer,
    query=prompt,
    history=[],
    images=[image],
    template_version='chat'
)

inputs = {
    'input_ids': input_by_model['input_ids'].unsqueeze(0).to(DEVICE),
    'token_type_ids': input_by_model['token_type_ids'].unsqueeze(0).to(DEVICE),
    'attention_mask': input_by_model['attention_mask'].unsqueeze(0).to(DEVICE),
    'images': [[input_by_model['images'][0].to(DEVICE).to(TORCH_TYPE)]] if image is not None else None,
}

gen_kwargs = {
    "max_new_tokens": 512,
    "pad_token_id": 128002,
}

with torch.no_grad():
    outputs = model.generate(**inputs, **gen_kwargs)
    outputs = outputs[:, inputs['input_ids'].shape[1]:]
    response = tokenizer.decode(outputs[0])
    response = response.split("<|end_of_text|>")[0]
    print("\nCogVLM2:", response)