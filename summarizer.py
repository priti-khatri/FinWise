import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["openai_api_key"])

def summarizer_interface():
    st.subheader("📝 Summarize Financial Text")

    st.markdown('<div class="card-container">', unsafe_allow_html=True)

    article = st.text_area("Paste any finance article, report, or explanation you'd like summarized:", height=200)

    if st.button("Summarize"):
        if article.strip():
            with st.spinner("Reading and summarizing your content... 📖"):
                try:
                    response = client.responses.create(
                        model="gpt-5-nano",
                        input=f"Summarize this in simple points: {article}",
                        store=False
                    )
                    st.markdown(f'<div class="card"><h4>Summary</h4><p>{response.output_text}</p></div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Couldn't summarize due to: {e}")
        else:
            st.warning("Please paste some text to summarize.")

    st.markdown('</div>', unsafe_allow_html=True)
