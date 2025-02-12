# Voice-Enabled Chatbot

## Overview
This is a fully voice-enabled chatbot that allows users to interact using spoken English. The system integrates advanced AI-driven speech processing and natural language understanding to provide real-time voice interactions with minimal latency.

### Key Components:
1. **Speech-to-Text (ASR)**: Converts user speech into text.
2. **Large Language Model (LLM)**: Processes text input and generates intelligent responses.
3. **Text-to-Speech (TTS)**: Converts chatbot responses into natural-sounding speech.

---

## Features
✅ **End-to-end voice-based interaction**
- **STT (Speech-to-Text)**: Implemented using Whisper AI and Assembly AI.
- **TTS (Text-to-Speech)**: Uses Coqui AI, Hugging Face T5, and ElevenLabs.
<br>
✅ **Supports natural language understanding via LLM**
- Integrated with Groq AI and OpenAI.
<br>
✅ **Low-latency response generation**
- Optimized using asynchronous processing.
<br>
✅ **Modular and extensible architecture**
- Allows easy customization and integration with other AI services.

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

---

## API Endpoints
The chatbot provides the following REST API endpoints:

| Endpoint  | Description |
|-----------|-------------|
| `/asr`    | Converts speech to text |
| `/llm`    | Processes text using LLM |
| `/tts`    | Converts text to speech |

---

## Project Structure
```
│── check/
│   ├── stt_to_tts.ipynb         # STT to TTS flow test
│   ├── asr_whisper_check.py      # Speech-to-Text (Whisper AI)
│   ├── asr_check.py              # Speech-to-Text (Assembly AI)
│   ├── llm_check.py              # Language Model Processing (Groq AI)
│   ├── tts_check.py              # Text-to-Speech (Coqui AI)
│   ├── tts_hf_check.py           # Text-to-Speech (Hugging Face T5)
│── utils.py                      # Utility functions for STT, LLM, and TTS
│── streamlit.py                   # Frontend implementation (Streamlit)
│── FastAPI.py                     # Backend implementation (FastAPI)
│── openAPI_utils.py               # OpenAI utilities for STT, LLM, and TTS
│── openAPI_streamlit.py           # Alternative frontend (Streamlit with OpenAI)
│── openAPI_FastAPI.py             # Alternative backend (FastAPI with OpenAI)
│── requirements.txt               # Project dependencies
│── README.md                      # Documentation
```

---

## Technologies Used
- **Speech-to-Text (ASR)**: Whisper AI, Assembly AI
- **LLM (AI Processing)**: Groq AI, OpenAI GPT API
- **Text-to-Speech (TTS)**: Coqui AI, Hugging Face T5, ElevenLabs
- **Backend Framework**: FastAPI
- **Frontend Framework**: Streamlit
- **Async Processing**: WebSockets, asyncio

---

## Contribution Guidelines

1. Fork the repository and create a new branch (`feature/your-feature`).
2. Commit your changes and push to GitHub.
3. Create a Pull Request (PR) for review.

---

## Contact
For inquiries, please reach out to [sharinmpshafna@gmail.com](mailto:sharinmpshafna@gmail.com).

