import streamlit as st
from openai import OpenAI
from lottie_util import display_lottie

def summarizer_interface():
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    st.header("📝 FinWise Summarizer")
    display_lottie(
        "https://assets1.lottiefiles.com/packages/lf20_7x7m9v.json",
        height=110,
        key="summarizer"
    )

    user_text = st.text_area("Paste any article, news, or report here:")

    if st.button("Summarize") and user_text.strip():
        with st.spinner("Summarizing..."):
            prompt = f"Summarize the following text in bullet points:\n\n{user_text}"

            try:
                completion = client.chat.completions.create(
                    model="gpt-4o-mini",  
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=200
                )

                summary = completion.choices[0].message.content.strip()
                st.success(summary)

            except Exception as e:
                st.error(f"⚠️ Error during summarization: {str(e)}")
