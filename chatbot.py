import streamlit as st
from lottie_util import display_lottie
import openai

def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="FinWise Chatbot", layout="wide", page_icon="💬")
load_css()

if "dark" not in st.session_state:
    st.session_state["dark"] = False
if st.button("Toggle Dark Mode"):
    st.session_state["dark"] = not st.session_state["dark"]
if st.session_state["dark"]:
    st.markdown("<style>body { background: #181926 !important; color: #e0e0e0 !important; } .glass-card { background: rgba(30,30,40,0.7) !important; color: #fff !important; } </style>", unsafe_allow_html=True)
else:
    st.markdown("<style>body { background: #f1f3f6 !important; color: #222 !important; } .glass-card { background: rgba(255,255,255,0.6) !important; color: #222 !important; } </style>", unsafe_allow_html=True)

openai.api_key = st.secrets["OPENAI_API_KEY"]

st.title("FinWise Chatbot – Ask Anything")

if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("Ask Me Anything")
    display_lottie("https://assets6.lottiefiles.com/packages/lf20_vfbbn2br.json", height=200, key="chatbot-lottie")
    user_input = st.text_input("Type your question here:")
    if st.button("Send") and user_input:
        with st.spinner("Thinking..."):
            messages = [{"role": "system", "content": "You are a helpful finance assistant."}]
            for speaker, text in st.session_state["chat_history"]:
                messages.append({"role": "user" if speaker=="You" else "assistant", "content": text})
            messages.append({"role": "user", "content": user_input})
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=256
            )
            bot_reply = response["choices"][0]["message"]["content"].strip()
            st.session_state["chat_history"].append(("You", user_input))
            st.session_state["chat_history"].append(("Bot", bot_reply))
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("Chat History")
    for speaker, text in st.session_state["chat_history"]:
        st.write(f"**{speaker}:** {text}")
    st.markdown('</div>', unsafe_allow_html=True)