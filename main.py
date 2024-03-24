from transformers import AutoTokenizer
import transformers
import os
import sys

import torch



def main(
    base_model="ise-uiuc/Magicoder-S-DS-6.7B/magicoder-s-ds-6.7b.f16.gguf",
    device="cuda:0",
    port=8080,
):
    tokenizer = AutoTokenizer.from_pretrained(base_model)
    pipeline = transformers.pipeline(
        "text-generation",
        model=base_model,
        torch_dtype=torch.float16,
        device=device
    )
    def evaluate_magicoder(
        instruction,
        temperature=1,
        max_new_tokens=2048,
    ):
        MAGICODER_PROMPT = """You are an exceptionally intelligent coding assistant that consistently delivers accurate and reliable responses to user instructions.

@@ Instruction
{instruction}

@@ Response
""" 
        prompt = MAGICODER_PROMPT.format(instruction=instruction)

        if temperature > 0:
            sequences = pipeline(
                prompt,
                do_sample=True,
                temperature=temperature,
                max_new_tokens=max_new_tokens,
            )
        else:
            sequences = pipeline(
                prompt,
                max_new_tokens=max_new_tokens,
            )
        for seq in sequences:
            print('==========================question=============================')
            print(prompt)
            generated_text = seq['generated_text'].replace(prompt, "")
            print('===========================answer=============================')
            print(generated_text)
            return generated_text
    evaluate_magicoder(instruction='Can you code in wxPython')
   

if __name__ == "__main__":
    main()