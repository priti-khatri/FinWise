import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["openai_api_key"])

def chatbot_interface():
    st.subheader("💬 Ask Finance Buddy")

    with st.container():
        st.markdown('<div class="card-container">', unsafe_allow_html=True)

        prompt = st.text_input("Ask anything about finance 👇")
        if st.button("Get Answer"):
            if prompt:
                with st.spinner("Thinking... 💡"):
                    try:
                        res = client.responses.create(
                            model="gpt-5-nano",
                            input=prompt,
                            store=False
                        )
                        st.markdown(f'<div class="card">{res.output_text}</div>', unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"Something went wrong: {e}")

        st.markdown('</div>', unsafe_allow_html=True)
