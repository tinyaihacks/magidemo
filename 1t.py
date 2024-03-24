from transformers import AutoModelForCausalLM, AutoTokenizer

# Replace with the path to your downloaded model file
model_path = "magicoder-s-ds-6.7b.gguf"

# Load the model and tokenizer
model = AutoModelForCausalLM.from_pretrained(model_path)
tokenizer = AutoTokenizer.from_pretrained('ise-uiuc/Magicoder-S-DS-6.7B')

# Generate text
prompt = "This is a prompt for the Magicoder model."
input_ids = tokenizer.encode(prompt, return_tensors="pt")
output = model.generate(input_ids)
generated_text = tokenizer.decode(output[0], skip_special_tokens=True)

print(generated_text)