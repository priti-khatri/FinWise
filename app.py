import streamlit as st
from chatbot import chatbot_interface
from glossary import glossary_interface
from recommender import recommender_interface
from explainer import explainer_interface
from investment_tips import investment_tips_interface
from summarizer import summarizer_interface
from scenario import scenario_interface
import utils

# Load custom CSS
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

def main():
    st.set_page_config(page_title="Finance Buddy", layout="wide", initial_sidebar_state="expanded")
    local_css("styles.css")

    # Sidebar with Dark Mode toggle and navigation
    st.sidebar.title("Finance Buddy")
    st.sidebar.markdown("Helping GenZ grow financially smart! 🚀")

    # Dark mode toggle
    dark_mode = st.sidebar.checkbox("Enable Dark Mode", value=True)
    if dark_mode:
        st.markdown('<body class="dark-mode">', unsafe_allow_html=True)
    else:
        st.markdown('<body class="light-mode">', unsafe_allow_html=True)

    # Navigation options
    page = st.sidebar.radio(
        "Navigate",
        (
            "🤖 Chatbot",
            "📖 Glossary",
            "🎯 Recommender",
            "💡 Explain Concepts",
            "📈 Investment Tips",
            "📝 Summarizer",
            "🔮 Scenario Simulator"
        )
    )

    # Visitor count (fake for now)
    st.sidebar.markdown("---")
    st.sidebar.markdown("👥 **50+ users today**")

    # Render pages
    if page == "🤖 Chatbot":
        chatbot_interface()
    elif page == "📖 Glossary":
        glossary_interface()
    elif page == "🎯 Recommender":
        recommender_interface()
    elif page == "💡 Explain Concepts":
        explainer_interface()
    elif page == "📈 Investment Tips":
        investment_tips_interface()
    elif page == "📝 Summarizer":
        summarizer_interface()
    elif page == "🔮 Scenario Simulator":
        scenario_interface()

    # Footer
    st.markdown("---")
    st.markdown(
        "<center>Made with ❤️ for GenZ | Powered by OpenAI API | Finance Buddy </center>",
        unsafe_allow_html=True,
    )


if __name__ == "__main__":
    main()
