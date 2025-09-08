import streamlit as st
from lottie_util import display_lottie
import openai

def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

st.set_page_config(page_title="FinWise Recommender", layout="wide", page_icon="🤖")
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

st.title("FinWise Recommender")

col1, col2 = st.columns(2)
with col1:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("Get a Recommendation")
    display_lottie("https://assets5.lottiefiles.com/packages/lf20_w51pcehl.json", height=200, key="recommender-lottie")
    age = st.number_input("Your age", min_value=18, max_value=100, value=30)
    goal = st.selectbox("Main financial goal", ["Retirement", "Buy a House", "Emergency Fund", "Travel", "Education"])
    risk = st.selectbox("Risk Tolerance", ["Low", "Medium", "High"])
    if st.button("Recommend for Me"):
        with st.spinner("Analyzing..."):
            prompt = (
                f"I am {age} years old. My main goal is '{goal}'. My risk tolerance is '{risk}'. "
                "Suggest a personalized investment or financial product for me, in 3-4 sentences."
            )
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200,
            )
            recommendation = response["choices"][0]["message"]["content"].strip()
            st.session_state["recommendation"] = recommendation
    st.markdown('</div>', unsafe_allow_html=True)

with col2:
    st.markdown('<div class="glass-card">', unsafe_allow_html=True)
    st.header("Our Suggestion")
    if "recommendation" in st.session_state:
        st.write(st.session_state["recommendation"])
    else:
        st.write("Fill in your details and click the button to see our suggestion!")
    st.markdown('</div>', unsafe_allow_html=True)