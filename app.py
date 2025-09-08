import streamlit as st
from lottie_util import display_lottie
from chatbot import chatbot_interface
from glossary import glossary_interface
from recommender import recommender_interface
from explainer import explainer_interface
from investment_tips import investment_tips_interface
from summarizer import summarizer_interface
from scenario import scenario_interface

def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def landing_page():
    st.markdown("""
    <div class='hero-header'>
      <div class='hero-title'>FinWise 💸</div>
      <div class='hero-sub'>
        Elevate your financial journey.<br>
        Modern tools. Instant advice.<br>
        <span style='color:#f806cc;font-weight:600;'>Built for GenZ. </span>
      </div>
    </div>
    """, unsafe_allow_html=True)
    display_lottie("https://assets2.lottiefiles.com/packages/lf20_49rdyysj.json", height=300, key="hero_lottie")

def main():
    st.set_page_config(page_title="FinWise", layout="wide", page_icon="💸")
    load_css()
    if "dark" not in st.session_state:
        st.session_state.dark = False
    st.sidebar.title("🌈 FinWise")
    if st.sidebar.button("🌙 Toggle Dark Mode"):
        st.session_state.dark = not st.session_state.dark
    body_class = "dark-mode" if st.session_state.dark else ""
    st.markdown(f'<div class="{body_class}">', unsafe_allow_html=True)
    pages = {
        "🏠 Home": landing_page,
        "💬 Chatbot": chatbot_interface,
        "📚 Glossary": glossary_interface,
        "✨ Recommender": recommender_interface,
        "🧠 Explain Concept": explainer_interface,
        "💡 Investment Tips": investment_tips_interface,
        "📝 Summarize": summarizer_interface,
        "📊 Scenario": scenario_interface,
    }
    choice = st.sidebar.radio("🚀 Navigation", list(pages.keys()))
    pages[choice]()
    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
