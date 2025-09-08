import streamlit as st

def chatbot_interface():
    st.markdown("<div style='background: rgba(0,0,0,0.5); border-radius: 15px; padding: 2rem;'>", unsafe_allow_html=True)
    st.title("🤖 Finance Chatbot - Ask me anything!")

    st.markdown("""
        <p style='color:#00CFFF;'>
        Type your finance, investment banking, or stock market questions below. 
        I’ll do my best to provide clear and useful answers!
        </p>
    """, unsafe_allow_html=True)

    user_input = st.text_input("Your question:", placeholder="E.g. What is an ETF?")

    if user_input:
        # Dummy response for demonstration — replace with AI integration!
        response = f"Great question! Here’s a quick answer for: **{user_input}**"
        st.markdown(f"<div style='color:#FFD700; font-weight:bold; margin-top:10px;'>{response}</div>", unsafe_allow_html=True)

    st.markdown("</div>", unsafe_allow_html=True)
