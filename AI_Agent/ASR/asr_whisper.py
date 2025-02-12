import whisper
import gradio as gr

model = whisper.load_model("small")

def transcribe(audio):
    
    #time.sleep(3)
    # load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(audio)
    audio = whisper.pad_or_trim(audio)

    # make log-Mel spectrogram and move to the same device as the model
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # detect the spoken language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # decode the audio
    options = whisper.DecodingOptions(fp16 = False)
    result = whisper.decode(model, mel, options)
    return result.text
    
    
 
import whisper
import gradio as gr

# Load Whisper model
model = whisper.load_model("base")

def transcribe(audio):
    # Load audio and pad/trim it to fit 30 seconds
    audio = whisper.load_audio(audio)
    audio = whisper.pad_or_trim(audio)

    # Convert to log-Mel spectrogram
    mel = whisper.log_mel_spectrogram(audio).to(model.device)

    # Detect language
    _, probs = model.detect_language(mel)
    print(f"Detected language: {max(probs, key=probs.get)}")

    # Decode audio
    options = whisper.DecodingOptions()
    result = whisper.decode(model, mel, options)
    return result.text

# Create Gradio interface
gr.Interface(
    title="OpenAI Whisper ASR Gradio Web UI",
    fn=transcribe,
    inputs=gr.Audio(type="filepath"),  # ✅ Fix: Removed 'source'
    outputs=gr.Textbox(),  
    live=True
).launch()