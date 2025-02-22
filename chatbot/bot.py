import random
import json
from chatbot.nlp_utils import preprocess_text
from difflib import get_close_matches

# Load intents from the JSON file
with open('chatbot/intents.json') as file:
    intents = json.load(file)

def get_response(user_input):
    user_input = preprocess_text(user_input)

    all_patterns = [pattern.lower() for intent in intents['intents'] for pattern in intent['patterns']]
    closest_match = get_close_matches(user_input.lower(), all_patterns, n=1, cutoff=0.7)

    if closest_match:
        for intent in intents['intents']:
            if closest_match[0] in map(str.lower, intent['patterns']):    
                return random.choice(intent['responses'])
    return "I'm not sure how to respond to that. Can you rephrase?"