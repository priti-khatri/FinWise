import streamlit as st
from openai import OpenAI
from lottie_util import display_lottie


def chatbot_interface():

    # Initialize OpenAI client
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    st.header("💬 FinWise Chatbot")
    display_lottie("https://assets6.lottiefiles.com/packages/lf20_vfbbn2br.json",
                   height=110, key="chatbot")

    # Initialize chat history
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    # User input box
    user_input = st.text_input("Ask FinWise anything about finance:", key="chatbox")

    # Avoid duplicate API calls on page reload
    if "last_message" not in st.session_state:
        st.session_state["last_message"] = ""

    # Send message
    if st.button("Send") and user_input and user_input != st.session_state["last_message"]:

        st.session_state["last_message"] = user_input  # prevent re-trigger on reruns

        with st.spinner("FinWise is thinking..."):

            # Prepare message history
            messages = [{"role": "system",
                         "content": "You are FinWise, a smart and friendly finance assistant. Keep answers simple, clear and practical."}]

            for speaker, text in st.session_state["chat_history"]:
                messages.append({
                    "role": "user" if speaker == "You" else "assistant",
                    "content": text
                })

            # Add new message
            messages.append({"role": "user", "content": user_input})

            # OpenAI ChatCompletions call
            completion = client.chat.completions.create(
                model="gpt-4o-mini",     # Best lightweight model for finance chatbot
                messages=messages,
                max_tokens=300
            )

            bot_reply = completion.choices[0].message.content.strip()

            # Update conversation history
            st.session_state["chat_history"].append(("You", user_input))
            st.session_state["chat_history"].append(("FinWise", bot_reply))

    # Display chat history
    st.subheader("Chat History")
    for speaker, text in st.session_state["chat_history"]:
        st.markdown(f"**{speaker}:** {text}")
