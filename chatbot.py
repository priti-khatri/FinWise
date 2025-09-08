# chatbot.py

import streamlit as st
import openai
import os

# Load your OpenAI API key securely
openai.api_key = st.secrets["OPENAI_API_KEY"] if "OPENAI_API_KEY" in st.secrets else os.getenv("OPENAI_API_KEY")

# Define the system message for the chatbot's personality
system_prompt = """
You are GenZ Finance Buddy – a helpful, friendly, and jargon-free finance guide.
Explain financial topics (like investment banking, debt, stocks, taxes) in clear, fun, simple language.
Use emojis, Gen Z slang, memes (when appropriate), and avoid overly technical jargon unless asked.
"""

def ask_gpt(question, chat_history):
    messages = [{"role": "system", "content": system_prompt}] + chat_history + [{"role": "user", "content": question}]

    try:
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",  # or gpt-4 if available in your account
            messages=messages,
            temperature=0.7,
            max_tokens=500
        )
        return response.choices[0].message["content"]
    except Exception as e:
        return f"🚨 Oops! Something went wrong: {str(e)}"

def chat_interface():
    st.subheader("🤖 Talk to GenZ Finance Buddy")

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    # Display chat history
    for message in st.session_state.chat_history:
        with st.chat_message(message["role"]):
            st.markdown(message["content"])

    # Input box for user's message
    user_input = st.chat_input("Ask me anything about finance 💸")

    if user_input:
        # Add user message
        st.session_state.chat_history.append({"role": "user", "content": user_input})

        # Get bot reply
        bot_reply = ask_gpt(user_input, st.session_state.chat_history)
        st.session_state.chat_history.append({"role": "assistant", "content": bot_reply})

        # Display bot reply
        with st.chat_message("assistant"):
            st.markdown(bot_reply)
