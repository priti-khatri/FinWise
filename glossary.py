import streamlit as st
from lottie_util import display_lottie
import openai

def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="FinWise Glossary", layout="wide", page_icon="📖")
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

st.title("FinWise Glossary")

terms = [
    "ETF", "Stock", "Bond", "Mutual Fund", "Inflation", "Compound Interest", "Risk Tolerance",
    "Expense Ratio", "Asset Allocation", "Dividend", "Index Fund", "Robo-Advisor"
]
col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("Select a Financial Term")
    term = st.selectbox("Choose a term:", terms)
    display_lottie("https://assets6.lottiefiles.com/packages/lf20_2znxv3dx.json", height=200, key="glossary-lottie")
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("Definition")
    if term:
        if st.button("Get Definition"):
            with st.spinner("Looking up..."):
                prompt = f"Explain the financial term '{term}' in simple language for a beginner."
                response = openai.ChatCompletion.create(
                    model="gpt-3.5-turbo",
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=150,
                )
                definition = response["choices"][0]["message"]["content"].strip()
                st.write(definition)
    st.markdown('</div>', unsafe_allow_html=True)