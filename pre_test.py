## Imports
#from huggingface_hub import hf_hub_download
from llama_cpp import Llama
from os.path import join
MAGICODER_PROMPT = """You are an exceptionally intelligent coding assistant that consistently delivers accurate and reliable responses to user instructions.

@@ Conversation History

{history}

@@ Instruction

{instruction}

@@ Response

"""

## Download the GGUF model
model_path = join( 'models', 'milkowski', 'Magicoder-S-DS-6.7B-GGUF', 'magicoder-s-ds-6.7b.f16.gguf')
## Instantiate model from downloaded file
llm = Llama(
    model_path=model_path,
    #n_ctx=16000,     n_threads=0,     n_gpu_layers=32,     use_cuda=True 
    n_gpu_layers=32, n_threads=0, n_ctx=3584, n_batch=521, use_cuda=True
)

## Generation kwargs
generation_kwargs = {
    "max_tokens":20000,
    "stop":["</s>"],
    "echo":True, # Echo the prompt in the output
    "top_k":1 # This is essentially greedy decoding, since the model will always return the highest-probability token. Set this value > 1 for sampling decoding
}

conversation_history = ""

while True:

    instruction = input("Enter your code instruction (or type 'quit' to exit): ")

    # Check if the user wants to quit
    if instruction.lower() == 'quit':
        break
        
    ## Run inference
    prompt = MAGICODER_PROMPT.format(history=conversation_history, instruction=instruction)

    res = llm(prompt, **generation_kwargs) # Res is a dictionary

    ## Unpack and the generated text from the LLM response dictionary and print it
    generated_response = res["choices"][0]["text"]
    print(generated_response)
    # res is short for result
    
    print('Done.')
    conversation_history += f"User: {instruction}\nAssistant: {generated_response}\n"