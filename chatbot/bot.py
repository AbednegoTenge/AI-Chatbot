import random
import json
from chatbot.nlp_utils import preprocess_text
from difflib import get_close_matches

# Load intents from the JSON file
with open('chatbot/intents.json') as file:
    intents = json.load(file)

def get_response(user_input):
    user_tokens = set(preprocess_text(user_input).split())

    for intent in intents['intents']:
        for pattern in intent['patterns']:
            pattern_tokens = set(pattern.lower().split())
            if user_tokens.intersection(pattern_tokens):
                return random.choice(intent['responses'])
    return "I'm not sure how to respond to that. Can you rephrase?"