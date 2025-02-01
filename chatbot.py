from flask import Flask, request, jsonify, send_from_directory
from googlesearch import search

app = Flask(__name__)

# Sample responses for the chatbot
responses = {
    "hello": "Hello! I'm your AI health coach. How can I assist you today?",
    "what should i eat": "I recommend a balanced diet with plenty of fruits and vegetables.",
    "how can i lose weight": "Regular exercise and a healthy diet are key to losing weight.",
    "tell me a workout plan": "A good plan includes cardio, strength training, and flexibility exercises.",
    "bye": "Goodbye! Stay healthy!"
}

def google_search(query):
    """Perform a Google search and return a summary text result."""
    try:
        results = search(query, num_results=5)  # Get the top 5 results
        summary = []
        for result in results:
            summary.append(result)  # Append the result URL to the summary

        # Join the summaries into a single string to return
        return "Here are some useful links: " + ', '.join(summary)
    except Exception as e:
        return f"Error occurred during search: {str(e)}"

@app.route('/')
def index():
    return send_from_directory('.', 'index.html')  # Serve index.html from the current directory

@app.route('/chatbot', methods=['POST'])
def chatbot():
    user_message = request.json.get('message', '').strip().lower()  # Get user message
    response_message = responses.get(user_message)

    if response_message is None:  # If no predefined response, perform Google search
        response_message = google_search(user_message)
    
    return jsonify({"response": response_message})

if __name__ == '__main__':
    app.run(debug=True)
