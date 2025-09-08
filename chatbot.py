import streamlit as st
import openai
import utils

def chatbot_interface():
    st.title("🤖 Finance Buddy Chatbot")

    openai.api_key = st.secrets["openai_api_key"]

    if "messages" not in st.session_state:
        st.session_state.messages = [{"role": "system", "content": "You are a helpful finance assistant for GenZ."}]

    with st.form(key="chat_form", clear_on_submit=True):
        user_input = st.text_input("Ask me anything about finance, stocks, investment banking...")
        submit = st.form_submit_button("Send")

    if submit and user_input:
        st.session_state.messages.append({"role": "user", "content": user_input})
        with st.spinner("Generating response..."):
            response = utils.get_openai_response(st.session_state.messages)
        st.session_state.messages.append({"role": "assistant", "content": response})

    for msg in st.session_state.messages:
        if msg["role"] == "user":
            st.markdown(f"<p style='color:#7C4DFF;'><b>You:</b> {msg['content']}</p>", unsafe_allow_html=True)
        elif msg["role"] == "assistant":
            st.markdown(f"<p style='color:#03DAC5;'><b>Finance Buddy:</b> {msg['content']}</p>", unsafe_allow_html=True)
