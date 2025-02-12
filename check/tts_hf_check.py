import os
import base64
import streamlit as st
import torch
from transformers import pipeline
from datasets import load_dataset
import soundfile as sf

# Load the text-to-speech model
synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts")

# Load speaker embeddings dataset
embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)

def text_to_speech(input_text):
    """
    Converts text to speech using Hugging Face's SpeechT5 TTS model and saves it as an audio file.
    """
    try:
        # Generate speech from text
        speech = synthesiser(input_text, forward_params={"speaker_embeddings": speaker_embedding})

        # Define output audio file path
        audio_file_path = "temp_audio_play.wav"

        # Save generated speech as a WAV file
        sf.write(audio_file_path, speech["audio"], samplerate=speech["sampling_rate"])

        # Ensure the file was successfully created
        if not os.path.exists(audio_file_path):
            raise FileNotFoundError("TTS failed to generate the audio file.")

        return audio_file_path
    except Exception as e:
        st.error(f"Error generating speech: {e}")
        return None  # Return None if there is an error

def autoplay_audio(file_path: str):
    """
    Embeds audio in Streamlit for autoplay.
    """
    try:
        with open(file_path, "rb") as f:
            data = f.read()
        b64 = base64.b64encode(data).decode("utf-8")
        md = f"""
        <audio autoplay controls>
        <source src="data:audio/wav;base64,{b64}" type="audio/wav">
        </audio>
        """
        st.markdown(md, unsafe_allow_html=True)
    except Exception as e:
        st.error(f"Error embedding audio: {e}")

# Streamlit UI
st.title("Text-to-Speech 🎙️")

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
