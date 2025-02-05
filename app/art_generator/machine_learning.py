from transformers import GPT2LMHeadModel, GPT2Tokenizer

# Charger le modèle pré-entrainé GPT-2
tokenizer = GPT2Tokenizer.from_pretrained("gpt2")
model = GPT2LMHeadModel.from_pretrained("gpt2")

def generate_description():
    # Créer un prompt pour décrire une œuvre d'art
    prompt = "Cette œuvre d'art représente"
    inputs = tokenizer.encode(prompt, return_tensors="pt")
    
    # Générer une description
    outputs = model.generate(inputs, max_length=100, num_return_sequences=1)
    description = tokenizer.decode(outputs[0], skip_special_tokens=True)
    
    # Retourner la description générée
    return description
