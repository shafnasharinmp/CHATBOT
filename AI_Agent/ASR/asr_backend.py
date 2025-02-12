from fastapi import FastAPI, File, UploadFile, HTTPException
import os
import assemblyai as aai
import shutil

# Initialize FastAPI app
app = FastAPI(title="Speech-to-Text API")

# Set AssemblyAI API key
aai.settings.api_key = os.getenv("ASSEMBLYAI_API_KEY")

@app.post("/speech-to-text")
async def speech_to_text(file: UploadFile = File(...)):
    """
    Converts uploaded speech (audio file) to text using AssemblyAI.
    """
    try:
        # Save uploaded file temporarily
        temp_audio_path = f"temp_{file.filename}"
        with open(temp_audio_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        # Transcribe using AssemblyAI
        transcriber = aai.Transcriber()
        transcript = transcriber.transcribe(temp_audio_path)

        # Remove the temporary file after processing
        os.remove(temp_audio_path)

        return {"transcription": transcript.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error transcribing audio: {e}")

# Run FastAPI server (for local testing)
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000)
