import streamlit as st
import openai
from lottie_util import display_lottie

def explainer_interface():
    client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    st.header("🧠 FinWise Explainer")
    display_lottie("https://assets9.lottiefiles.com/packages/lf20_9wpyhdzo.json", height=110, key="explainer")
    user_concept = st.text_input("Enter a finance concept to explain (e.g. 'ETFs', 'inflation'):")
    if st.button("Explain"):
        with st.spinner("Explaining..."):
            prompt = f"Explain '{user_concept}' in simple language for a beginner."
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=250,
            )
            expl = response.choices[0].message.content.strip()
            st.success(expl)