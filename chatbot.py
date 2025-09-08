import streamlit as st
from lottie_util import display_lottie

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
    st.markdown(
        "<style>body { background: #181926 !important; color: #e0e0e0 !important; } "
        ".glass-card { background: rgba(30,30,40,0.7) !important; color: #fff !important; } </style>",
        unsafe_allow_html=True
    )
else:
    st.markdown(
        "<style>body { background: #f1f3f6 !important; color: #222 !important; } "
        ".glass-card { background: rgba(255,255,255,0.6) !important; color: #222 !important; } </style>",
        unsafe_allow_html=True
    )

st.title("FinWise Chatbot")

col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("Ask Me Anything")
    display_lottie("https://assets6.lottiefiles.com/packages/lf20_vfbbn2br.json", height=200, key="chatbot-lottie")
    st.write("Type your financial questions below and get instant AI-powered answers!")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("Chat History")
    # (Placeholder for chat history or chat UI)
    st.write("Your previous questions and answers will appear here.")
    st.markdown('</div>', unsafe_allow_html=True)