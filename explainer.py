import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["openai_api_key"])

def explainer_interface():
    st.header("Explain a Finance Term")

    with st.container():
        st.markdown('<div class="card-container">', unsafe_allow_html=True)
        term = st.text_input("Enter term:")
        if st.button("Explain"):
            if term:
                res = client.responses.create(model="gpt-5-nano", input=term, store=False)
                st.markdown(f'<div class="card">{res.output_text}</div>', unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
