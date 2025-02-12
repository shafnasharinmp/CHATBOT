import streamlit as st
import requests

# FastAPI Backend URL
API_URL = "http://127.0.0.1:8000/transcribe/"

st.title("🎙️ Whisper ASR - Speech to Text")
st.write("Upload an audio file and get its transcription.")

# File uploader
uploaded_file = st.file_uploader("Upload an audio file", type=["wav", "mp3", "m4a"])

if uploaded_file:
    st.audio(uploaded_file, format="audio/wav")
    
    # Send file to FastAPI for transcription
    files = {"file": uploaded_file.getvalue()}
    response = requests.post(API_URL, files=files)
    
    if response.status_code == 200:
        data = response.json()
        st.write(f"**Detected Language:** {data['language']}")
        st.write(f"**Transcription:** {data['transcription']}")
    else:
        st.error("Error in transcription. Please try again.")
