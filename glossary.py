import streamlit as st
from openai import OpenAI
from lottie_util import display_lottie


def glossary_interface():

    #  OpenAI client 
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    st.header("📖 FinWise Glossary")
    display_lottie(
        "https://assets6.lottiefiles.com/packages/lf20_2znxv3dx.json",
        height=110,
        key="glossary"
    )

    # finance terms
    terms = [
        "ETF", "Stock", "Bond", "Mutual Fund", "Inflation", "Compound Interest",
        "Risk Tolerance", "Expense Ratio", "Asset Allocation", "Dividend",
        "Index Fund", "Robo-Advisor"
    ]

    term = st.selectbox("Choose a term:", terms)

    if st.button("Get Definition"):
        with st.spinner("Looking up..."):

            prompt = (
                f"Provide a simple, beginner-friendly explanation of the finance term: {term}. "
                f"Include an example."
            )

            # api call
            completion = client.chat.completions.create(
                model="gpt-4o-mini",     # stable + cheap
                messages=[{"role": "user", "content": prompt}],
                max_tokens=150
            )

            definition = completion.choices[0].message.content.strip()

        st.success(definition)
