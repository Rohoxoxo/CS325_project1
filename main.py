# main.py

# Import required libraries
from transformers import AutoModelForCausalLM, AutoTokenizer, pipeline

# Function to load a model and tokenizer
def load_model(model_name):
    print(f"Loading model: {model_name}")
    tokenizer = AutoTokenizer.from_pretrained(model_name)
    model = AutoModelForCausalLM.from_pretrained(model_name)
    return pipeline("text-generation", model=model, tokenizer=tokenizer)

# List of prompts
prompts = [
    "A shocking Chinese AI advancement called DeepSeek is sending US stocks plunging",
    "As sales slump, Kohl’s turns to a new CEO to bring back customers",
    "Expect record-high egg prices for most of the year"
]

# Load GPT-2
gpt2_model_name = "gpt2"  # Verified public model
gpt2 = load_model(gpt2_model_name)

# Load DistilGPT-2
distilgpt2_model_name = "distilgpt2"  # Verified public model
distilgpt2 = load_model(distilgpt2_model_name)

# Generate responses and save to file
def generate_and_save_responses(model, model_name):
    with open(f"{model_name}_responses.txt", "w") as f:
        for prompt in prompts:
            print(f"Generating response for: {prompt}")
            response = model(prompt, max_length=100, do_sample=True, truncation=True, pad_token_id=50256)[0]['generated_text']
            f.write(f"Prompt: {prompt}\n")
            f.write(f"Response: {response}\n\n")
    print(f"Responses saved to {model_name}_responses.txt")

# Run for both models
generate_and_save_responses(gpt2, "GPT2")
generate_and_save_responses(distilgpt2, "DistilGPT2")
