
from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("ise-uiuc/Magicoder-S-DS-6.7B")
model = AutoModelForCausalLM.from_pretrained("ise-uiuc/Magicoder-S-DS-6.7B",
                                              torch_dtype=torch.bfloat16)

# Move the model to GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

prompt='''
write wxpython app that loads jupyter notebook and displays it in tree control . 
add button to execute a cellof notebook, and text control to display results of each execution. do not give me outline. 
 show full python code code
'''

# Encode the prompt
input_ids = tokenizer.encode(prompt, return_tensors="pt")

# Move the input_ids tensor to GPU
input_ids = input_ids.to(device)

# Generate tokens one by one
for _ in range(1024):
    outputs = model(input_ids)
    next_token_id = outputs.logits[0, -1].argmax().item()
    input_ids = torch.cat([input_ids, torch.tensor([[next_token_id]], device=device)], dim=-1)
    
    token = tokenizer.decode(next_token_id)
    print(token, end="", flush=True)
    
    if next_token_id == tokenizer.eos_token_id:
        break
        