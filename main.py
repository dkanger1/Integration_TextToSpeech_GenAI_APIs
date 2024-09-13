from flask import Flask, render_template, jsonify, send_file, request
import os
import requests
import pygame
import openai
from mock import chat_with_gpt, generate_audio
from dotenv import load_dotenv
import pyaudio
import wave
import numpy as np 

# from controller import generate_audio, chat_with_gpt
load_dotenv()

OPENAI_GPT_TOKEN = os.getenv('OPENAI_GPT_TOKEN')
ELEVENLABS_API_TOKEN = os.getenv('ELEVENLABS_API_TOKEN')
print(OPENAI_GPT_TOKEN)
print(ELEVENLABS_API_TOKEN)
openai.api_key = OPENAI_GPT_TOKEN
# Initialize pygame mixer
pygame.mixer.init()
app = Flask(__name__)

CHUNK_SIZE = 1024
VOICE_ID = "7u8qsX4HQsSHJ0f8xsQZ"
OUTPUT_PATH = "output6.mp3"

@app.route('/')
def index():
    return render_template('index.html')


@app.route('/chat')
def chat():
    return render_template('index.html')

@app.route('/send_message', methods=['POST'])
def send_message():
    user_message = request.json['message']
    response = chat_with_gpt(user_message)
    audio_path = generate_audio(response)
    if audio_path:
        return jsonify({'response': response, 'audio_url': '/play_audio?path=' + audio_path})
    else:
        return jsonify({'response': response, 'error': 'Falha ao gerar áudio'}), 500

@app.route('/play_audio')
def play_audio():
    audio_path = request.args.get('path')
    if os.path.exists(audio_path):
        return send_file(audio_path, mimetype="audio/mpeg")
    else:
        return "Audio file not found", 404


if __name__ == '__main__':
    app.run(debug=True)