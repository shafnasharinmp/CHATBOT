from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import os
import base64
import torch
import tempfile
from TTS.api import TTS

# Initialize FastAPI app
app = FastAPI(title="Text-to-Speech API")

# Check for CUDA availability
device = "cuda" if torch.cuda.is_available() else "cpu"

# Pydantic model for input
class TextToSpeechRequest(BaseModel):
    text: str

@app.post("/text-to-speech")
def text_to_speech_endpoint(request: TextToSpeechRequest):
    """
    Converts text to speech using Coqui TTS and returns Base64 encoded audio.
    """
    try:
        # Initialize TTS model
        tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=False).to(device)
        
        # Create a temporary file for storing generated audio
        with tempfile.NamedTemporaryFile(delete=False, suffix=".mp3") as temp_audio:
            audio_path = temp_audio.name
        
        # Generate speech and save it as an audio file
        tts.tts_to_file(text=request.text, file_path=audio_path)

        # Read and encode the audio file in Base64
        with open(audio_path, "rb") as f:
            audio_data = f.read()
        b64_audio = base64.b64encode(audio_data).decode("utf-8")

        # Delete the temporary file
        os.remove(audio_path)

        return {"audio_base64": b64_audio}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating speech: {e}")

# Run FastAPI server (for local testing)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
