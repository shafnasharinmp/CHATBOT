import os
import base64
import streamlit as st
from dotenv import load_dotenv
import assemblyai as aai
from TTS.api import TTS
import torch


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

# Streamlit UI
st.title("Text-to-Speech 🤖")

# User input text
input_text = st.text_area("Enter text to convert to speech:")

if st.button("Generate Audio"):
    with st.spinner("Generating audio response..."):
        if input_text.strip():
            audio_file = text_to_speech(input_text)
            if audio_file:  # Only proceed if the file was successfully created
                autoplay_audio(audio_file)
                st.write(input_text)  # Display input text
                st.session_state.messages = st.session_state.get("messages", [])
                st.session_state.messages.append({"role": "assistant", "content": input_text})

                # Safely delete the file after use
                try:
                    os.remove(audio_file)
                except FileNotFoundError:
                    st.warning("The audio file was not found for deletion.")
        else:
            st.warning("Please enter some text before generating speech.")
