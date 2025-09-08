import streamlit as st
import openai

def chatbot_interface():
    st.title("💬 FinWise AI Chatbot")

    st.markdown("""
        <style>
        .chat-container {
            background-color: #f3f4f6;
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 15px;
        }
        .user-msg {
            background-color: #e0f7fa;
            padding: 10px;
            border-radius: 10px;
            margin-bottom: 5px;
        }
        .bot-msg {
            background-color: #ede7f6;
            padding: 10px;
            border-radius: 10px;
        }
        </style>
    """, unsafe_allow_html=True)

    openai.api_key = st.secrets["OPENAI_API_KEY"]

    if "chat_history" not in st.session_state:
        st.session_state.chat_history = []

    user_input = st.text_input("Ask FinWise something about finance, budgeting, or investments:")

    if st.button("Send"):
        if user_input:
            st.session_state.chat_history.append({"role": "user", "content": user_input})

            try:
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=st.session_state.chat_history
                )
                reply = response.choices[0].message.content
                st.session_state.chat_history.append({"role": "assistant", "content": reply})
            except Exception as e:
                st.error("Error fetching response from AI.")

    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            st.markdown(f"<div class='user-msg'><strong>You:</strong> {msg['content']}</div>", unsafe_allow_html=True)
        else:
            st.markdown(f"<div class='bot-msg'><strong>FinWise:</strong> {msg['content']}</div>", unsafe_allow_html=True)
