import streamlit as st
from lottie_util import display_lottie
import openai

def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="FinWise Scenario", layout="wide", page_icon="📊")
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

st.title("FinWise Scenario Simulator")

col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("Describe Your Scenario")
    display_lottie("https://assets2.lottiefiles.com/packages/lf20_b7xv6h5r.json", height=200, key="scenario-lottie")
    scenario = st.text_area("Describe a financial scenario to simulate (e.g., \"If I invest $500/month for 10 years at 7% return...\")")
    if st.button("Simulate") and scenario:
        with st.spinner("Simulating..."):
            prompt = f"Analyze this personal finance scenario and provide projected results in 3-5 bullet points: {scenario}"
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=220,
            )
            st.session_state["scenario_result"] = response["choices"][0]["message"]["content"].strip()
    st.markdown('</div>', unsafe_allow_html=True)
with col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("Scenario Results")
    if "scenario_result" in st.session_state:
        st.write(st.session_state["scenario_result"])
    else:
        st.write("Describe your scenario and click Simulate to see results here.")
    st.markdown('</div>', unsafe_allow_html=True)