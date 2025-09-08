import streamlit as st
from lottie_util import display_lottie
import openai

def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="FinWise Explainer", layout="wide", page_icon="🧠")
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

st.title("FinWise Explainer")

topics = [
    "How does compound interest work?",
    "What is asset allocation?",
    "How do ETFs differ from mutual funds?",
    "What are the basics of stock market investing?",
    "How does inflation affect purchasing power?",
    "What is dollar-cost averaging?"
]

col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("Choose a Topic")
    topic = st.selectbox("Select a topic to explain:", topics)
    display_lottie("https://assets9.lottiefiles.com/packages/lf20_9wpyhdzo.json", height=200, key="explainer-lottie")
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("Explanation")
    if topic:
        if st.button("Explain Topic"):
            with st.spinner("Explaining..."):
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": f"Explain this to a beginner: {topic}"}],
                    max_tokens=250,
                )
                expl = response["choices"][0]["message"]["content"].strip()
                st.write(expl)
    st.markdown('</div>', unsafe_allow_html=True)