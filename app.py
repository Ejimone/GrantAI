import asyncio
import openai #Make sure to install this package
import requests #Make sure to install this package
from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/process_audio', methods=['POST'])
async def process_audio():
    if 'audio' not in request.files:
        return jsonify({'error': 'No audio file provided'}), 400

    audio_file = request.files['audio']
    audio_data = await audio_file.read()

    try:
        # Transcribe audio using OpenAI
        transcription = await openai.transcribe_audio(audio_data)

        # Send transcription to main.py (or your chatbot API)
        response = requests.post('http://localhost:8080/chat', json={'message': transcription})
        response.raise_for_status() # Raise HTTPError for bad responses (4xx or 5xx)
        chatbot_response = response.json()['response'] #Assumes your API returns JSON with a 'response' key. Adjust accordingly

        return jsonify({'response': chatbot_response})

    except openai.OpenAIError as e:
        return jsonify({'error': f'OpenAI Error: {e}'}), 500
    except requests.exceptions.RequestException as e:
        return jsonify({'error': f'Chatbot API Error: {e}'}), 500  # Handle network/API errors
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True, port=5000) #Explicitly set the port to 5000
