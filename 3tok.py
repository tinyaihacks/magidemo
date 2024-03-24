from transformers import AutoTokenizer, AutoModelForCausalLM
import torch

MAGICODER_PROMPT = """You are an exceptionally intelligent coding assistant that consistently delivers accurate and reliable responses to user instructions.

@@ Conversation History

{history}

@@ Instruction

{instruction}

@@ Response

"""

# Load the tokenizer and model
tokenizer = AutoTokenizer.from_pretrained("ise-uiuc/Magicoder-S-DS-6.7B")
model = AutoModelForCausalLM.from_pretrained("milkowski/Magicoder-S-DS-6.7B-GGUF/magicoder-s-ds-6.7b.f16.gguf",
                                              torch_dtype=torch.bfloat16)

# Move the model to GPU
device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
model = model.to(device)

# Initialize conversation history
conversation_history = ""

while True:
    # Get user input
    instruction = input("Enter your code instruction (or type 'quit' to exit): ")

    # Check if the user wants to quit
    if instruction.lower() == 'quit':
        break

    # Format the prompt with the conversation history and user's instruction
    prompt = MAGICODER_PROMPT.format(history=conversation_history, instruction=instruction)

    # Encode the prompt
    input_ids = tokenizer.encode(prompt, return_tensors="pt")

    # Move the input_ids tensor to GPU
    input_ids = input_ids.to(device)

    # Generate tokens one by one
    generated_response = ""
    for _ in range(1024):
        outputs = model(input_ids)
        next_token_id = outputs.logits[0, -1].argmax().item()
        input_ids = torch.cat([input_ids, torch.tensor([[next_token_id]], device=device)], dim=-1)

        token = tokenizer.decode(next_token_id)
        generated_response += token
        print(token, end="", flush=True)

        if next_token_id == tokenizer.eos_token_id:
            break

    print()

    # Update the conversation history
    conversation_history += f"User: {instruction}\nAssistant: {generated_response}\n"