import streamlit as st
from chatbot import chat_interface
from glossary import glossary_interface
from recommender import recommendation_interface
from trends import trend_interface

# Load custom CSS for styling
def load_css():
    with open("assets/style.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="GenZ Finance Buddy", layout="wide", page_icon="💸")
    load_css()

    st.sidebar.image("assets/logo.png", width=150)
    st.sidebar.title("📚 Navigation")
    page = st.sidebar.radio(
        "Choose a page:",
        ("🏠 Home", "📖 Finance Glossary", "🤖 Ask AI", "🎯 Personalized Path", "📈 Trends")
    )

    st.markdown("<h1 style='text-align: center;'>🧠 GenZ Finance Buddy</h1>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center;'>Learn, Explore, and Ask Anything About Money 💰</p>", unsafe_allow_html=True)

    if page == "🏠 Home":
        st.image("https://i.imgur.com/O3ZC5pL.png", use_column_width=True)
        st.markdown("""
        ### Welcome GenZ!
        - 📊 Learn about past vs. present financial realities
        - 🤖 Use AI to get personalized learning and answers
        - 📚 Demystify finance jargon
        - 🔥 Build your financial confidence!
        """)
    elif page == "📖 Finance Glossary":
        glossary_interface()
    elif page == "🤖 Ask AI":
        chat_interface()
    elif page == "🎯 Personalized Path":
        recommendation_interface()
    elif page == "📈 Trends":
        trend_interface()

if __name__ == "__main__":
    main()
