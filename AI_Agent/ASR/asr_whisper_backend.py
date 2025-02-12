from fastapi import FastAPI, File, UploadFile
import whisper
import uvicorn
import os

# Initialize FastAPI
app = FastAPI()

# Load Whisper model
model = whisper.load_model("base")

@app.post("/transcribe/")
async def transcribe_audio(file: UploadFile = File(...)):
    """
    Transcribes an uploaded audio file using OpenAI's Whisper model.
    """
    # Save uploaded file temporarily
    temp_file = f"temp_{file.filename}"
    with open(temp_file, "wb") as audio_file:
        audio_file.write(await file.read())

    # Load and process audio
    audio = whisper.load_audio(temp_file)
    audio = whisper.pad_or_trim(audio)
    
    # Convert to log-Mel spectrogram
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # Detect language
    _, probs = model.detect_language(mel)
    detected_lang = max(probs, key=probs.get)

    # Decode the audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)

    # Clean up temp file
    os.remove(temp_file)

    return {"language": detected_lang, "transcription": result.text}

# Run the FastAPI app
if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000) #why host
