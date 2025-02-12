# audio_preprocessing.py
import librosa
import soundfile as sf
import noisereduce as nr
import json

def preprocess_audio(file_path, output_path):
    audio, sr = librosa.load(file_path, sr=None)
    # Resample
    if sr != 16000:
        audio = librosa.resample(audio, sr, 16000)
        sr = 16000
    # Noise reduction
    reduced_noise = nr.reduce_noise(y=audio, sr=sr)
    # Trim silence
    non_silence_indices = librosa.effects.split(reduced_noise, top_db=20)
    trimmed_audio = [reduced_noise[start:end] for start, end in non_silence_indices]
    sf.write(output_path, trimmed_audio[0], sr)

def annotate_dataset(audio_files, transcriptions):
    dataset = [{"audio_file": audio, "transcription": transcription} for audio, transcription in zip(audio_files, transcriptions)]
    with open('dataset.json', 'w') as f:
        json.dump(dataset, f, ensure_ascii=False, indent=4)
