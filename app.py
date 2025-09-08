import streamlit as st
import os

# Import your page modules
from chatbot import chatbot_interface
from glossary import glossary_interface
from recommender import recommender_interface
from trends import trend_interface

# Set page config
st.set_page_config(
    page_title="FinWise | GenZ Finance Buddy 💸",
    page_icon="💸",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Inject CSS for background and fonts
def set_background_and_style():
    # Background image from Unsplash - finance themed
    unsplash_url = "https://source.unsplash.com/1600x900/?finance,stock,investment,money"
    css = f"""
    <style>
    .stApp {{
        background-image: url("{unsplash_url}");
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        color: white;
        font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
        padding-top: 2rem;
        padding-bottom: 3rem;
    }}
    .stSidebar {{
        background-color: #0e1117;
        color: white;
        padding-top: 1rem;
        padding-bottom: 1rem;
    }}
    .block-container {{
        background: rgba(0, 0, 0, 0.5);
        border-radius: 15px;
        padding: 2rem;
    }}
    /* Animated GIF as sidebar header */
    .sidebar-gif {{
        width: 150px;
        margin-left: auto;
        margin-right: auto;
        display: block;
        border-radius: 10px;
        margin-bottom: 1rem;
    }}
    </style>
    """
    st.markdown(css, unsafe_allow_html=True)

def home_page():
    st.markdown("<h1 style='text-align: center;'>💼 Welcome to FinWise — Your GenZ Finance Buddy!</h1>", unsafe_allow_html=True)
    st.markdown(
        """
        <p style="font-size:18px; text-align:center;">
        Learn investment banking, finance, and stock market terms in a fun and interactive way.<br>
        Get personalized recommendations based on your income and knowledge.<br>
        Stay updated with market trends and boost your financial literacy!
        </p>
        """,
        unsafe_allow_html=True
    )

    # Show a finance-related animated GIF on home page (centered)
    gif_url = "https://media.giphy.com/media/3o7TKsQciqEdjMaXz6/giphy.gif"  # cool finance money animation from Giphy
    st.image(gif_url, width=350, caption="Stay curious, keep learning! 🚀")

    st.markdown("---")
    st.markdown(
        """
        ### Get Started:
        - Use the sidebar to navigate between **Chatbot**, **Glossary**, **Recommender**, and **Trends**.
        - Ask questions, explore terms, and discover your personalized finance journey!
        """
    )

def main():
    set_background_and_style()

    st.sidebar.title("📌 Navigate")

    # Display animated GIF in sidebar header instead of logo image
    gif_sidebar = "https://media.giphy.com/media/3o7TKsQciqEdjMaXz6/giphy.gif"
    st.sidebar.markdown(
        f'<img src="{gif_sidebar}" class="sidebar-gif" alt="Finance Animation">',
        unsafe_allow_html=True
    )

    page = st.sidebar.radio(
        "Go to",
        ["🏠 Home", "🤖 Chatbot", "📖 Glossary", "🎯 Recommender", "📊 Trends"],
        index=0
    )

    # Render page based on selection
    if page == "🏠 Home":
        home_page()
    elif page == "🤖 Chatbot":
        chatbot_interface()
    elif page == "📖 Glossary":
        glossary_interface()
    elif page == "🎯 Recommender":
        recommender_interface()
    elif page == "📊 Trends":
        trend_interface()

    st.markdown("---")
    st.markdown(
        "<center>🚀 Built with ❤️ by GenZ, for GenZ — Finance made simple.</center>",
        unsafe_allow_html=True
    )

if __name__ == "__main__":
    main()
