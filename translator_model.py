from transformers import MarianMTModel, MarianTokenizer

# Point to your local model directory
model_path = "./model_local"

def get_supported_languages():
    return ["Local Translator"]  # single local model

def load_translation_model(language_pair):
    tokenizer = MarianTokenizer.from_pretrained(model_path)
    model = MarianMTModel.from_pretrained(model_path)
    return tokenizer, model
