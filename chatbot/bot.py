import random
import nltk
from chatbot.nlp_utils import preprocess_text

responses = {
    "greeting": ["Hello!", "Hi there!", "Hey!"],
    "goodbye": ["Goodbye!", "See you later!", "Bye!"],
    "default": ["I'm not sure how to respond to that. Can you rephrase?"]
}

def get_response(user_input):
    user_input = preprocess_text(user_input)

    if "hello" in user_input or 'hi' in user_input:
        return random.choice(responses["greeting"])
    elif "bye" in user_input or 'goodbye' in user_input:
        return random.choice(responses['goodbye'])
    else:
        return random.choice(responses["default"])