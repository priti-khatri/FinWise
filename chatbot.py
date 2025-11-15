import streamlit as st
from openai import OpenAI
from lottie_util import display_lottie


def chatbot_interface():

    #  OpenAI client
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    st.header("💬 FinWise Chatbot")
    display_lottie(
        "https://assets6.lottiefiles.com/packages/lf20_vfbbn2br.json",
        height=110,
        key="chatbot"
    )

    # chat history
    if "chat_history" not in st.session_state:
        st.session_state["chat_history"] = []

    if "last_message" not in st.session_state:
        st.session_state["last_message"] = ""

    st.markdown("### Ask FinWise Anything About Finance")
    user_input = st.text_input("Your message:", key="chatbox")

    # Send message
    if st.button("Send") and user_input:

        # duplicate triggering on rerun
        if user_input != st.session_state["last_message"]:
            st.session_state["last_message"] = user_input

            with st.spinner("FinWise is thinking..."):

                # Prepare formatted message history
                messages = [{
                    "role": "system",
                    "content": (
                        "You are FinWise, a friendly and knowledgeable personal "
                        "finance assistant. Keep answers simple and clear."
                    )
                }]

                for speaker, text in st.session_state["chat_history"]:
                    messages.append({
                        "role": "user" if speaker == "You" else "assistant",
                        "content": text
                    })

                messages.append({"role": "user", "content": user_input})

                # Chat Completion
                completion = client.chat.completions.create(
                    model="gpt-4o-mini",
                    messages=messages,
                    max_tokens=300
                )

                bot_reply = completion.choices[0].message.content.strip()

                # Save to history
                st.session_state["chat_history"].append(("You", user_input))
                st.session_state["chat_history"].append(("FinWise", bot_reply))

    # Chat UI
    st.markdown("### Chat History")
    chat_container = st.container()

    with chat_container:
        for speaker, text in st.session_state["chat_history"]:

            if speaker == "You":
                st.markdown(
                    f"""
                    <div style="
                        background-color:#E3F2FD;
                        padding:10px;
                        border-radius:8px;
                        margin-bottom:8px;
                        text-align:left;
                        border-left:4px solid #2196F3;
                    ">
                        <b>You:</b> {text}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

            else:
                st.markdown(
                    f"""
                    <div style="
                        background-color:#F1F8E9;
                        padding:10px;
                        border-radius:8px;
                        margin-bottom:8px;
                        text-align:left;
                        border-left:4px solid #4CAF50;
                    ">
                        <b>FinWise:</b> {text}
                    </div>
                    """,
                    unsafe_allow_html=True
                )

    # Clear chat button
    if st.button("Reset Chat"):
        st.session_state["chat_history"] = []
        st.session_state["last_message"] = ""
        st.experimental_rerun()
