import streamlit as st
import openai
from lottie_util import display_lottie

def glossary_interface():
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    st.header("📖 FinWise Glossary")
    display_lottie("https://assets6.lottiefiles.com/packages/lf20_2znxv3dx.json", height=110, key="glossary")
    terms = [
        "ETF", "Stock", "Bond", "Mutual Fund", "Inflation", "Compound Interest", "Risk Tolerance",
        "Expense Ratio", "Asset Allocation", "Dividend", "Index Fund", "Robo-Advisor"
    ]
    term = st.selectbox("Choose a term:", terms)
    if st.button("Get Definition"):
        with st.spinner("Looking up..."):
            prompt = f"Explain the financial term '{term}' in simple language for a beginner."
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150,
            )
            definition = response["choices"][0]["message"]["content"].strip()
            st.success(definition)