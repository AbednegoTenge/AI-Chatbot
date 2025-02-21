from flask import Flask, request, jsonify, render_template
from chatbot.bot import get_response

app = Flask(__name__)


@app.route('/')
def home():
    return "Welcome to the AI Chatbot"

@app.route('/chat', methods=['GET', 'POST'])
def chat():
    if request.method == 'POST':
        user_message = request.json.get('message')
        response = get_response(user_message)
        return jsonify({'response': response})
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)