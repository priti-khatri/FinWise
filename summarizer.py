import streamlit as st
from lottie_util import display_lottie

def summarizer_interface():
    st.markdown(
        """
        <div class="glass-card">
            <h2 style='color:#4cc9f0;font-size:2.2em;letter-spacing:1px;'>
                📝 Summarize Anything
            </h2>
            <p style='font-size:1.16em;'>Drop some text and we'll TL;DR it for you! ⚡</p>
        </div>
        """, unsafe_allow_html=True
    )
    display_lottie("https://assets10.lottiefiles.com/packages/lf20_7fw2gk0r.json", height=120, key="sum_lottie")
    text = st.text_area("Paste your long article or paragraph here:")
    if st.button("Summarize"):
        if text:
            st.success("Here's your TL;DR: (Add your summarizer logic here!)")