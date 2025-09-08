import streamlit as st
from lottie_util import display_lottie

def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="FinWise Summarizer", layout="wide", page_icon="📝")
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

st.title("FinWise Summarizer")

col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("Summary Generator")
    display_lottie("https://assets1.lottiefiles.com/packages/lf20_7x7m9v.json", height=200, key="summarizer-lottie")
    st.write("Summarize financial news, articles, or reports instantly.")
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("Key Points")
    # (Placeholder for summary points)
    st.write("Highlights and main takeaways will show here.")
    st.markdown('</div>', unsafe_allow_html=True)