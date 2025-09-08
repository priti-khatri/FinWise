import streamlit as st
from chatbot import chatbot_interface
from glossary import glossary_interface
from recommender import recommender_interface
from trends import trends_interface
from portfolio import portfolio_tracker
from news import get_finance_news

st.set_page_config(
    page_title="FinWise – Your Finance Buddy 💸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
    <style>
    .main {
        background: linear-gradient(135deg, #f6f0ff, #e0f7fa);
        color: #333;
        font-family: 'Poppins', sans-serif;
    }
    .block-container {
        padding: 2rem 2rem 2rem 2rem;
    }
    .sidebar .sidebar-content {
        background: rgba(255, 255, 255, 0.85);
    }
    </style>
""", unsafe_allow_html=True)

st.sidebar.image("https://img.icons8.com/color/96/finance.png", width=80)
st.sidebar.title("FinWise 💼")
nav = st.sidebar.radio("Navigate", ["🤖 Chatbot", "📖 Glossary", "🎯 Recommender", "📈 Trends", "📂 Portfolio", "📰 News"])

if nav == "🤖 Chatbot":
    chatbot_interface()
elif nav == "📖 Glossary":
    glossary_interface()
elif nav == "🎯 Recommender":
    recommender_interface()
elif nav == "📈 Trends":
    trends_interface()
elif nav == "📂 Portfolio":
    portfolio_tracker()
elif nav == "📰 News":
    get_finance_news()
