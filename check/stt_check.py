import os
import assemblyai as aai
import streamlit as st
from audio_recorder_streamlit import audio_recorder

# Set AssemblyAI API key
aai.settings.api_key = "b6f84c667ca6403da5956edcb46b966d"

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

# Streamlit UI
st.title("Speech to Text 🤖")

# Create footer container for the microphone
footer_container = st.container()
with footer_container:
    audio_bytes = audio_recorder()

if audio_bytes:
    # Save the recorded audio to a temporary file
    audio_file_path = "temp_audio.mp3"
    with open(audio_file_path, "wb") as f:
        f.write(audio_bytes)

    with st.spinner("Transcribing..."):
        transcript = speech_to_text(audio_file_path)
        st.write(transcript)

    # Remove the temporary file after processing
    os.remove(audio_file_path)
