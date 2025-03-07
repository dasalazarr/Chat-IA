from flask import Flask, render_template, request, jsonify
from flask_socketio import SocketIO
import os
from dotenv import load_dotenv
import json
from models.openai_model import OpenAIModel
from models.anthropic_model import AnthropicModel
from models.google_model import GoogleModel
from utils.router import ModelRouter
from utils.response_mixer import ResponseMixer

# Load environment variables
load_dotenv()

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-secret-key')
socketio = SocketIO(app, cors_allowed_origins="*")

# Initialize models
openai_model = OpenAIModel(api_key=os.getenv('OPENAI_API_KEY'))
anthropic_model = AnthropicModel(api_key=os.getenv('ANTHROPIC_API_KEY'))
google_model = GoogleModel(api_key=os.getenv('GOOGLE_API_KEY'))

# Initialize router and mixer
router = ModelRouter([openai_model, anthropic_model, google_model])
mixer = ResponseMixer()

@app.route('/')
def index():
    """Render the main chat interface."""
    return render_template('index.html')

@socketio.on('send_message')
def handle_message(data):
    """Handle incoming chat messages."""
    user_message = data['message']
    
    # Route the message to the appropriate model(s)
    selected_models = router.route_query(user_message)
    responses = {}
    
    for model in selected_models:
        responses[model.name] = model.generate_response(user_message)
    
    # Mix responses if multiple models were used
    if len(responses) > 1:
        final_response = mixer.mix_responses(responses, user_message)
    else:
        model_name = list(responses.keys())[0]
        final_response = responses[model_name]
    
    # Send the response back to the client
    socketio.emit('receive_message', {
        'message': final_response,
        'models_used': list(responses.keys())
    })

@app.route('/api/chat', methods=['POST'])
def api_chat():
    """REST API endpoint for chat."""
    data = request.json
    user_message = data.get('message', '')
    
    if not user_message:
        return jsonify({'error': 'No message provided'}), 400
    
    # Route the message to the appropriate model(s)
    selected_models = router.route_query(user_message)
    responses = {}
    
    for model in selected_models:
        responses[model.name] = model.generate_response(user_message)
    
    # Mix responses if multiple models were used
    if len(responses) > 1:
        final_response = mixer.mix_responses(responses, user_message)
    else:
        model_name = list(responses.keys())[0]
        final_response = responses[model_name]
    
    return jsonify({
        'message': final_response,
        'models_used': list(responses.keys())
    })

if __name__ == '__main__':
    socketio.run(app, debug=True, host='0.0.0.0', port=int(os.getenv('PORT', 5000)))