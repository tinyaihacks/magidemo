## Imports
from llama_cpp import Llama
from os.path import join
import time

MAGICODER_PROMPT = """You are an exceptionally intelligent coding assistant that consistently delivers accurate and reliable responses to user instructions.

@@ Conversation History

{history}

@@ Instruction

{instruction}

@@ Response

"""

## Download the GGUF model
# caange it to 'magicoder-s-ds-6.7b.f16.gguf'
model_path = join('models', 'milkowski', 'Magicoder-S-DS-6.7B-GGUF', 'magicoder-s-ds-6.7b.f16.gguf')

## Instantiate model from downloaded file
llm = Llama(
    model_path=model_path,
    n_gpu_layers=32, n_threads=24, n_ctx=3584, n_batch=521, mlock=True, use_cuda=True
)

## Generation kwargs
generation_kwargs = {
    "max_tokens": 20000,
    "stop": ["</s>"],
    "echo": True,  # Echo the prompt in the output
    "top_k": 1,  # This is essentially greedy decoding, since the model will always return the highest-probability token. Set this value > 1 for sampling decoding
    "stream": True  # Enable streaming
}
 
conversation_history = ""

while True:
    instruction = input("Enter your code instruction (or type 'quit' to exit): ")
    
    # Check if the user wants to quit
    if instruction.lower() == 'quit':
        break
    
    ## Run inference
    prompt = MAGICODER_PROMPT.format(history=conversation_history, instruction=instruction)
    
    generated_response = ""
    start_time = old_time = time.time()
    buffer = ""
    for output in llm(prompt, **generation_kwargs):
        generated_text = output["choices"][0]["text"]
        generated_response += generated_text
        buffer += generated_text
        
        if "\n" in buffer:
            lines = buffer.split("\n")
            for line in lines[:-1]:
                elapsed_time = time.time() - start_time
                line_delta = elapsed_time -old_time
                print(f"[{elapsed_time:.2f}s][{line_delta:.2f}s] {line}")
                old_time=elapsed_time
            buffer = lines[-1]
    
    # Print any remaining text in the buffer
    if buffer:
        elapsed_time = time.time() - start_time
        print(f"[{elapsed_time:.2f}s] {buffer}")
    
    print()
    
    conversation_history += f"User: {instruction}\nAssistant: {generated_response}\n"
