from transformers import AutoModelForCausalLM, AutoTokenizer
from os.path import join

# Specify the path to the model file
model_path = join('models', 'milkowski', 'Magicoder-S-DS-6.7B-GGUF', 'magicoder-s-ds-6.7b.f16.gguf')

# Load the tokenizer
tokenizer = AutoTokenizer.from_pretrained('ise-uiuc/Magicoder-S-DS-6.7B')

# Load the model
model = AutoModelForCausalLM.from_pretrained('milkowski/Magicoder-S-DS-6.7B-GGUF/magicoder-s-ds-6.7b.f16.gguf')