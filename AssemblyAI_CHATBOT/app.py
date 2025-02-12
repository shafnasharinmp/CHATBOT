import assemblyai as aai
from elevenlabs import generate, stream
from openai import OpenAI
import os
from dotenv import load_dotenv
# from langchain_groq import ChatGroq
# from langchain_openai import ChatOpenAI
# from langchain_community.tools.tavily_search import TavilySearchResults
# from langgraph.prebuilt import create_react_agent
# from langchain_core.messages.ai import AIMessage

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
openai_client = OpenAI(api_key=api_key)

#GROQ_API_KEY = os.getenv("GROQAI_API_KEY")

class AI_Assistant:
    def __init__(self):
        aai.settings.api_key =  "ASSEMBLYAI-API-KEY"
        #self.openai_client = ChatGroq(model="llama-3.3-70b-versatile", api_key= GROQ_API_KEY)
        self.openai_client = OpenAI(api_key = "OPENAI-API-KEY")
        self.elevenlabs_api_key = "ELEVENLABS-API-KEY"

        self.transcriber = None

        # Prompt
        self.full_transcript = [
            {"role":"system", "content":"You are a AI CHATBOT Assistant. Be resourceful and efficient."},
        ]

###### Step 2: Real-Time Transcription with AssemblyAI ######
        
    def start_transcription(self):
        self.transcriber = aai.RealtimeTranscriber(
            sample_rate = 16000,
            on_data = self.on_data,
            on_error = self.on_error,
            on_open = self.on_open,
            on_close = self.on_close,
            end_utterance_silence_threshold = 1000
        )

        self.transcriber.connect()
        microphone_stream = aai.extras.MicrophoneStream(sample_rate =16000)
        self.transcriber.stream(microphone_stream)
    
    def stop_transcription(self):
        if self.transcriber:
            self.transcriber.close()
            self.transcriber = None

    def on_open(self, session_opened: aai.RealtimeSessionOpened):
        print("Session ID:", session_opened.session_id)
        return


    def on_data(self, transcript: aai.RealtimeTranscript):
        if not transcript.text:
            return

        if isinstance(transcript, aai.RealtimeFinalTranscript):
            self.generate_ai_response(transcript)
        else:
            print(transcript.text, end="\r")


    def on_error(self, error: aai.RealtimeError):
        print("An error occured:", error)
        return


    def on_close(self):
        #print("Closing Session")
        return

##### Step 3: Pass real-time transcript to OpenAI ######
    
    def generate_ai_response(self, transcript):

        self.stop_transcription()

        self.full_transcript.append({"role":"user", "content": transcript.text})
        print(f"\nPatient: {transcript.text}", end="\r\n")

        response = self.openai_client.chat.completions.create(
            model = "gpt-3.5-turbo",
            messages = self.full_transcript
        )

        ai_response = response.choices[0].message.content

        self.generate_audio(ai_response)

        self.start_transcription()
        print(f"\nReal-time transcription: ", end="\r\n")

# from groq import Groq

    # def generate_ai_response(self, transcript):
    #     """
    #     Processes user transcript, sends it to Groq AI, generates AI response,
    #     converts it to audio, and restarts transcription.
    #     """

    #     #  Stop transcription before processing
    #     self.stop_transcription()

    #     # Append user input to conversation history
    #     self.full_transcript.append({"role": "user", "content": transcript.text})
    #     print(f"\nPatient: {transcript.text}", end="\r\n")

    #     try:
    #             # Call Groq AI API
    #             response = self.openai_client.chat.completions.create(
    #                 model="llama-3.3-70b-versatile",  # Available models: llama3 , mixtral
    #                 messages=self.full_transcript
    #             )

    #             # Extract AI response
    #             ai_response = response.choices[0].message.content
    #             print(f"\nGroq AI Response: {ai_response}", end="\r\n")

    #             # Convert AI response to audio
    #             self.generate_audio(ai_response)

    #     except Exception as e:
    #             print(f"Error generating AI response: {e}")

    #         # Restart transcription
    #     self.start_transcription()
    #     print(f"\nReal-time transcription: ", end="\r\n")



###### Step 4: Generate audio with ElevenLabs ######
        
    def generate_audio(self, text):

        self.full_transcript.append({"role":"assistant", "content": text})
        print(f"\nAI: {text}")

        audio_stream = generate(
            api_key = self.elevenlabs_api_key,
            text = text,
            voice = "Rachel",
            stream = True
        )

        stream(audio_stream)

greeting = "Welcome, how may I assist you?"
ai_assistant = AI_Assistant()
ai_assistant.generate_audio(greeting)
ai_assistant.start_transcription()

        





    



    





