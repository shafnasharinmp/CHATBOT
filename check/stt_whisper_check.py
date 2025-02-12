import os
import base64
import torch
import whisper
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

import streamlit as st
import os
from audio_recorder_streamlit import audio_recorder
from streamlit_float import *



# Load Whisper model
model = whisper.load_model("small")
def speech_to_text(audio_path):
    """
    Converts speech (audio) to text using Whisper.
    """
    try:
        audio_data = whisper.load_audio(audio_path)
        audio_data = whisper.pad_or_trim(audio_data)
        mel = whisper.log_mel_spectrogram(audio_data).to(model.device)
        
        options = whisper.DecodingOptions()
        result = whisper.decode(model, mel, options)
        return result.text
    except Exception as e:
        print(f"Error transcribing audio: {e}")
        return ""
    
