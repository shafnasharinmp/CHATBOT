import os
import base64
import streamlit as st
from dotenv import load_dotenv
from groq import Groq
import assemblyai as aai
import torch
from TTS.api import TTS

# Set AssemblyAI API key
# ASSEMBLYAI_API_KEY = os.getenv("ASSEMBLYAI_API_KEY")
# aai.settings.api_key = ASSEMBLYAI_API_KEY
aai.settings.api_key = "b6f84c667ca6403da5956edcb46b966d"

# Load environment variables
# load_dotenv()
# #API_KEY = os.getenv("GROQ_API_KEY")
API_KEY = "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" 

client = Groq(api_key=API_KEY)

def get_answer(messages):
    """
    Uses Groq AI to generate a response based on user messages.
    """
    system_message = [{"role": "system", "content": "You are a helpful AI chatbot that answers user questions. Give the answer in short by default. Act as an AI chatbot who is smart and friendly"}]
    
    if isinstance(messages, str):
        messages = [{"role": "user", "content": messages}]
    
    messages = system_message + messages  # Combine system and user messages

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error calling Groq AI: {e}")
        return "I'm sorry, but I couldn't process your request."



def speech_to_text(audio_data):
    """
    Converts speech (audio) to text using AssemblyAI.
    """
    try:
        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(audio_data)
        return transcript.text
    except Exception as e:
        st.error(f"Error transcribing audio: {e}")
        return ""


# Check device (CPU/GPU) for TTS
device = "cuda" if torch.cuda.is_available() else "cpu"

def text_to_speech(input_text):
    """
    Converts input_text to speech using Coqui TTS and saves it as an audio file.
    """
    try:
        tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False).to(device)
        audio_file = os.path.join(os.getcwd(), "temp_audio_play.mp3")  # Use absolute path
        tts.tts_to_file(text=input_text, file_path=audio_file)

        # Ensure the file was created
        if not os.path.exists(audio_file):
            raise FileNotFoundError("TTS failed to generate the audio file.")

        return audio_file
    except Exception as e:
        st.error(f"Error generating speech: {e}")
        return None  # Return None instead of an empty string

def autoplay_audio(file_path: str):
    """
    Embeds audio in Streamlit for autoplay.
    """
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode("utf-8")
        md = f"""
        <audio autoplay>
        <source src="data:audio/mp3;base64,{b64}" type="audio/mp3">
        </audio>
        """
        st.markdown(md, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error embedding audio: {e}")