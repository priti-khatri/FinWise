import streamlit as st
from lottie_util import display_lottie

def chatbot_interface():
    st.markdown(
        """
        <div class="glass-card">
            <h2 style='color:#4361ee;font-size:2.2em;letter-spacing:1px;'>
                💬 Chat with FinWise Bot
            </h2>
            <p style='font-size:1.16em;'>Need advice? Ask me anything about finance! 🚀</p>
        </div>
        """, unsafe_allow_html=True
    )
    display_lottie("https://assets10.lottiefiles.com/packages/lf20_tutvdkg0.json", height=160, key="chatbot_lottie")
    user_input = st.text_input("What's on your mind? 🤔")
    if st.button("Send"):
        if user_input:
            st.success("Bot says: This is what I think about your query! (Replace with your bot logic)")