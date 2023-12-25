import os
from flask import Flask, render_template, request, jsonify
import vertexai
from vertexai.preview.generative_models import GenerativeModel

app = Flask(__name__)
PROJECT_ID = "kanesgpt"  
LOCATION = "asia-southeast1" 

vertexai.init(project=PROJECT_ID, location=LOCATION)

def create_session():
    chat_model = GenerativeModel("gemini-pro")
    chat = chat_model.start_chat()
    return chat

def response(chat, message):
    parameters = {
        "max_output_tokens": 2048,
        "temperature": 0.9,
        "top_p": 1
    }
    result = chat.send_message(message, generation_config=parameters)
    return result.text

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/gemini', methods=['GET', 'POST'])
def vertex_gemini():
    user_input = ""
    if request.method == 'GET':
        user_input = request.args.get('user_input')
    else:
        user_input = request.form['user_input']
    chat_model = create_session()
    content = response(chat_model,user_input)
    return jsonify(content=content)

if __name__ == '__main__':
    app.run(debug=True, port=8080, host='0.0.0.0')

# def run_chat():
#     chat_model = create_session()
#     print(f"Chat Session created")
    
#     while True:
#         user_input = input("You: ")
#         if user_input.lower() in ['exit', 'quit']:
#             break
        
#         content = response(chat_model, user_input)
#         print(f"AI: {content}")

# if __name__ == '__main__':
#     run_chat()