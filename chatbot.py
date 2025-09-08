import streamlit as st
import openai
from lottie_util import display_lottie

def chatbot_interface():
    client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    st.header("💬 FinWise Chatbot")
    display_lottie("https://assets6.lottiefiles.com/packages/lf20_vfbbn2br.json", height=110, key="chatbot")
    
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []
    user_input = st.text_input("Ask FinWise anything about finance:", key="chatbox")
    if st.button("Send", key="send_button") and user_input:
        with st.spinner("FinWise is typing..."):
            messages = [{"role": "system", "content": "You are a helpful finance assistant."}]
            for speaker, text in st.session_state["chat_history"]:
                messages.append({"role": "user" if speaker=="You" else "assistant", "content": text})
            messages.append({"role": "user", "content": user_input})
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=messages,
                max_tokens=256
            )
            bot_reply = response.choices[0].message.content.strip()
            st.session_state["chat_history"].append(("You", user_input))
            st.session_state["chat_history"].append(("FinWise", bot_reply))
    st.subheader("Chat History")
    for speaker, text in st.session_state["chat_history"]:
        st.markdown(f"**{speaker}:** {text}")