# Voice-Enabled Chatbot

## Overview
This is a fully voice-enabled chatbot that allows users to interact using spoken English. The system integrates advanced AI-driven speech processing and natural language understanding to provide real-time voice interactions with minimal latency.

### Key Components:
1. **Speech-to-Text (ASR)**: Converts user speech into text.
2. **Large Language Model (LLM)**: Processes text input and generates intelligent responses.
3. **Text-to-Speech (TTS)**: Converts chatbot responses into natural-sounding speech.

---

## Features
✔ End-to-end voice-based interaction
<br>
    - STT (Speech-to-Text): Implemented using Whisper AI and Assembly AI.
    <br>
    - TTS (Text-to-Speech): Uses Coqui AI, Hugging Face T5, and ElevenLabs.

✔ Supports natural language understanding via LLM
<br>
    - Integrated with Groq AI and OpenAI.

✔ Low-latency response generation
<br>
    - Optimized using asynchronous processing.

✔ Modular and extensible architecture
<br>
    - Allows easy customization and integration with other AI services.

---

## Project Structure
```

│── AI_Agent
│ ├── AI_LLM_Agent(OpenAI ,Groq & Tavily)/..
│ ├── ASR/..
│ ├── TTS/..
└── AssemblyAI_CHATBOT/
    ├── app.py
    ├── readme.md
    ├── requirements.txt
    ├── setup_windows.bat
    └── setup.sh
│── check/
│   ├── stt_to_tts.ipynb          
│   ├── asr_whisper_check.py     
│   ├── asr_check.py              
│   ├── llm_check.py             
│   ├── tts_check.py             
│   ├── tts_hf_check.py           
│── utils.py                      # Utility functions for STT, LLM, and TTS
│── streamlit_app.py              # Frontend implementation (Streamlit)
│── FastAPI.py                    # Backend implementation (FastAPI)
│── openAPI_utils.py              # OpenAI utilities for STT, LLM, and TTS
│── openAPI_streamlit.py          # Alternative frontend (Streamlit with OpenAI)
│── openAPI_FastAPI.py            # Alternative backend (FastAPI with OpenAI)
│── Docker_streamlit              # Docker for streamlit
│── Docker_streamlit_compose.py   # Docker compose for streamlit
│── LLM.ipynb                     # LLM implementation - eg
│── ASR_To_STT.ipynb              # ASR and STT implentation - eg
│── Ask_Qn.mp4                    # Result 
│── Give_Ans.mp4                  # Result
│── requirements.txt              # Project dependencies
│── README.md                     # Documentation
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

## Technologies Used
- Speech-to-Text (ASR): Whisper AI, Assembly AI
- LLM (AI Processing): Groq AI, OpenAI GPT API
- Text-to-Speech (TTS): Coqui AI, Hugging Face T5, ElevenLabs
- Backend Framework: FastAPI
- Frontend Framework: Streamlit
- Async Processing: WebSockets, asyncio

In my Draft :

Assembly AI : Speech-to-text transcription with advanced AI models.
Groq AI : High-speed inference for LLMs, optimizing AI performance(Low Latency).
Tavily AI : AI-driven web search and data extraction for real-time insights.
Coqui AI : open-source text-to-speech (TTS) models for lifelike voice synthesis.
ElevenLabs : AI-powered text-to-speech (TTS) with ultra-realistic voice synthesis.

---

## Resources
•	https://openai.com/index/whisper/<br>
•	https://github.com/coqui-ai/TTS<br>
•	https://www.gradio.app/guides/quickstart<br>
•	https://www.assemblyai.com/docs<br>
•	https://elevenlabs.io/docs/api-reference/introduction<br>
•	https://docs.tavily.com/guides/introduction<br>
•	https://console.groq.com/docs/speech-text<br>
•	https://cookbook.openai.com/examples/voice_solution<br>
•	https://fastapi.tiangolo.com/<br>
•	http://127.0.0.1:8000/redoc<br>
•	http://127.0.0.1:8000/docs

---

## Installation

**1. Clone the Repository**
```sh
git clone https://github.com/shafnasharinmp/CHATBOT.git
cd CHATBOT
```

**2. Install Dependencies**
```sh
pip install -r requirements.txt
```

**3. Run sample App**
```sh
streamlit run streamlit_app.py
```
---



## Contribution Guidelines

1. Fork the repository and create a new branch (`feature/your-feature`).
2. Commit your changes and push to GitHub.
3. Create a Pull Request (PR) for review.

---

## Contact
For inquiries, please reach out to [sharinmpshafna@gmail.com](mailto:sharinmpshafna@gmail.com).

