from transformers import pipeline
import torch

MAGICODER_PROMPT = """You are an exceptionally intelligent coding assistant that consistently delivers accurate and reliable responses to user instructions.

@@ Instruction
{instruction}

@@ Response
"""

instruction ='''
write wxpython app that loads jupyter notebook and displays it in tree control . 
add button to execute a cellof notebook, and text control to display results of each execution. do not give me outline. 
 show full python code code
'''
if 1:
    generator = pipeline(
        model="ise-uiuc/Magicoder-S-DS-6.7B",
        task="text-generation",
        torch_dtype=torch.bfloat16,
        device_map="auto",
    )
    
while True:
    # Get user input
    instruction = input("Enter your code instruction (or type 'quit' to exit): ")
    
    prompt = MAGICODER_PROMPT.format(instruction=instruction)

    result = generator(prompt, max_length=1024, num_return_sequences=1, temperature=0.0)
    print(result[0]["generated_text"])