import streamlit as st
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

def main():
    st.set_page_config(page_title="FinWise", layout="wide")
    load_css()

    st.sidebar.title("FinWise")
    
    pages = {
        "Chatbot": chatbot_interface,
        "Glossary": glossary_interface,
        "Recommender": recommender_interface,
        "Explain Concept": explainer_interface,
        "Investment Tips": investment_tips_interface,
        "Summarize": summarizer_interface,
        "Scenario": scenario_interface,
    }

    choice = st.sidebar.radio("Navigation", list(pages.keys()))
    pages[choice]()

    st.markdown("</div>", unsafe_allow_html=True)

if __name__ == "__main__":
    main()
