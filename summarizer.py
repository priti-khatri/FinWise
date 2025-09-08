import streamlit as st
import openai
from lottie_util import display_lottie

def summarizer_interface():
    client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    st.header("📝 FinWise Summarizer")
    display_lottie("https://assets1.lottiefiles.com/packages/lf20_7x7m9v.json", height=110, key="summarizer")
    user_text = st.text_area("Paste any article, news, or report here:")
    if st.button("Summarize"):
        with st.spinner("Summarizing..."):
            prompt = f"Summarize the following text in bullet points:\n\n{user_text}"
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200,
            )
            summary = response.choices[0].message.content.strip()
            st.success(summary)