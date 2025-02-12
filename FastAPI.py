from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List
import os
import base64
import assemblyai as aai
import torch
from TTS.api import TTS
from groq import Groq

# Initialize FastAPI app
app = FastAPI(title="AI Backend API")

# Set API Keys
aai.settings.api_key = "b6f84c667ca6403da5956edcb46b966d"
GROQ_API_KEY = "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"
client = Groq(api_key=GROQ_API_KEY)

device = "cuda" if torch.cuda.is_available() else "cpu"

# Pydantic Models
class ChatRequest(BaseModel):
    messages: List[str]

class SpeechRequest(BaseModel):
    audio_data: str  # Base64 encoded audio data

class TextToSpeechRequest(BaseModel):
    text: str

# AI Chat Endpoint
@app.post("/chat")
def chat_endpoint(request: ChatRequest):
    system_message = [{"role": "system", "content": "You are a smart AI chatbot."}]
    user_messages = [{"role": "user", "content": msg} for msg in request.messages]
    messages = system_message + user_messages
    
    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile", messages=messages
        )
        return {"response": response.choices[0].message.content}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Speech-to-Text Endpoint
@app.post("/speech-to-text")
def speech_to_text_endpoint(request: SpeechRequest):
    try:
        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(request.audio_data)
        return {"transcription": transcript.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Text-to-Speech Endpoint
@app.post("/text-to-speech")
def text_to_speech_endpoint(request: TextToSpeechRequest):
    try:
        tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC").to(device)
        audio_file = "temp_audio.mp3"
        tts.tts_to_file(text=request.text, file_path=audio_file)
        
        with open(audio_file, "rb") as f:
            data = f.read()
        b64_audio = base64.b64encode(data).decode("utf-8")
        
        return {"audio_base64": b64_audio}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Run FastAPI server (for local testing)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
