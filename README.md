# Voice-Enabled-CHATBOT

## Overview
This is a fully voice-enabled chatbot that allows users to interact using spoken English. The system integrates:

1. **Speech-to-Text (ASR)**: Transcribes user speech into text.
2. **Large Language Model (LLM)**: Processes text input and generates intelligent responses.
3. **Text-to-Speech (TTS)**: Converts chatbot responses into high-quality speech.

The chatbot ensures seamless real-time interactions with minimal latency.

---

## Features
✅ End-to-end voice-based interaction
- STT: Used Whisper AI and Aseembly AI
- TSS: Used Coqui AI,HuggingFace T5 and ElevenLabs
✅ Supports natural language understanding via LLM  - Used GroqAI and openAI 
✅ Low-latency response generation using asynchronous processing   
✅ Modular architecture for easy customization  

---

## Installation

### **1. Clone the Repository**
```sh
git clone https://github.com/your-username/voice-enabled-chatbot.git
cd voice-enabled-chatbot
```

### **2. Create a Virtual Environment (Optional)**
```sh
python -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate
```

### **3. Install Dependencies**
```sh
pip install -r requirements.txt
```

```

### **Endpoints**
from utils
| Endpoint  | Description |
|-----------|-------------|
| `/asr`    | Converts speech to text |
| `/llm`   | Processes text with LLM |
| `/tts`    | Converts text to speech |

---

## Project Structure
**```
│── check/
│   ├── stt_to_tts.ipython        # stt to tss flow
│   ├── asr_whisper_check.py         # Speech-to-Text ( Whisper)
│   ├── asr_check.py         # Speech-to-Text ( AsemblyAI )
│   ├── llm_check.py         # Language Model Processing( Groq AI)
│   ├── tts_check.py         # Text-to-Speech (Coqui AI)
│   ├── tts_hf_check.py         # Text-to-Speech(HuggingFace T5)
│── utils.py/            # stt,llm,tss
│── streamlit.py/        # Frontend
│── FastAPI.py/          #backend
│── openAPI_utils.py/            # stt,llm,tss
│── openAPI_streamlit.py/        # Frontend
│── openAPI_FastAPI.py/          #Backend
│── openAPI_requirements.txt   # Dependencies
│── requirements.txt   # Dependencies
│── README.md          # Documentation
```**

**---

## Technologies Used
- **Speech-to-Text (ASR)**: Google Cloud Speech-to-Text API
- **LLM (AI Processing)**: OpenAI GPT API
- **Text-to-Speech (TTS)**: Google Cloud Text-to-Speech API
- **Backend Framework**: FastAPI
- **Async Processing**: WebSockets, asyncio

---

## Contribution Guidelines

1. Fork the repository and create a new branch (`feature/your-feature`)
2. Commit your changes and push to GitHub
3. Create a Pull Request (PR) for review

---**


## Contact
For inquiries, please reach out to [sharinmpshafna@gmail.com](mailto:sharinmpshafna@gmail.com).

