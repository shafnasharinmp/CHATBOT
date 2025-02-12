import os
import base64y
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

client = Groq(api_key=API_KEY)


def get_answer(messages):
    """
    Uses Groq AI to generate a response based on user messages.
    """
    system_message = [{"role": "system", "content": "You are a helpful AI chatbot that answers user questions"}]
    
    if isinstance(messages, str):
        messages = [{"role": "user", "content": messages}]
    
    messages = system_message + messages  # Combine system and user messages

    try:
        response = client.chat.completions.create(
            model="llama-3.3-70b-versatile",
            messages=messages
        )
        return response.choices[0].message.content
    except Exception as e:
        print(f"Error calling Groq AI: {e}")
        return "I'm sorry, but I couldn't process your request."



meassage = get_answer("what is AI")
st.write(meassage)