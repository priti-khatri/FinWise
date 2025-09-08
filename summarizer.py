import streamlit as st
import openai
import utils

def summarizer_interface():
    st.title("📝 Finance Article & Concept Summarizer")

    openai.api_key = st.secrets["openai_api_key"]

    text = st.text_area("Paste finance article or concept text here to summarize:")

    if st.button("Summarize"):
        if text.strip():
            prompt = f"Summarize this finance content for a GenZ audience: {text}"
            with st.spinner("Summarizing..."):
                summary = utils.get_openai_response([{"role": "user", "content": prompt}])
            st.markdown(summary)
        else:
            st.warning("Please paste some text to summarize.")
