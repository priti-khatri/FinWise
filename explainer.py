import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["openai_api_key"])

def explainer_interface():
    st.subheader("🔎 Explain Financial Concepts")

    st.markdown('<div class="card-container">', unsafe_allow_html=True)

    topic = st.text_input("Enter a financial concept you'd like explained (e.g. How does SIP work?)")

    if st.button("Explain It"):
        if topic:
            with st.spinner("Crunching numbers and terms... 💭"):
                try:
                    response = client.responses.create(
                        model="gpt-5-nano",
                        input=f"Explain in simple terms: {topic}",
                        store=False
                    )
                    st.markdown(f'<div class="card"><h4>{topic}</h4><p>{response.output_text}</p></div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Oops! Something went wrong: {e}")
        else:
            st.warning("Please enter a topic to explain.")

    st.markdown('</div>', unsafe_allow_html=True)
