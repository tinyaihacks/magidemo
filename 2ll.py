## Imports
from huggingface_hub import hf_hub_download
from llama_cpp import Llama

## Download the GGUF model
model_name = "milkowski/Magicoder-S-DS-6.7B-GGUF"
model_file = "magicoder-s-ds-6.7b.f16.gguf" # this is the specific model file we'll use in this example. It's a 4-bit quant, but other levels of quantization are available in the model repo if preferred
model_path = hf_hub_download(model_name, filename=model_file)

## Instantiate model from downloaded file
llm = Llama(
    model_path=model_path,
    n_ctx=16000,  # Context length to use
    n_threads=32,            # Number of CPU threads to use
    n_gpu_layers=32        # Number of model layers to offload to GPU
)

## Generation kwargs
generation_kwargs = {
    "max_tokens":20000,
    "stop":["</s>"],
    "echo":False, # Echo the prompt in the output
    "top_k":1 # This is essentially greedy decoding, since the model will always return the highest-probability token. Set this value > 1 for sampling decoding
}

## Run inference
prompt = "can u code in wxpython "
res = llm(prompt, **generation_kwargs) # Res is a dictionary

## Unpack and the generated text from the LLM response dictionary and print it
print(res["choices"][0]["text"])
# res is short for result