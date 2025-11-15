import streamlit as st
from openai import OpenAI
from lottie_util import display_lottie


def explainer_interface():

    # Initialize OpenAI client using new syntax
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    st.header("🧠 FinWise Explainer")
    display_lottie(
        "https://assets9.lottiefiles.com/packages/lf20_9wpyhdzo.json",
        height=110,
        key="explainer"
    )

    user_concept = st.text_input(
        "Enter a finance concept to explain (e.g. 'ETFs', 'inflation'):"
    )

    if st.button("Explain") and user_concept:

        with st.spinner("Explaining..."):

            prompt = (
                f"Explain the concept '{user_concept}' in simple, beginner-friendly "
                f"language with examples. Keep it short and practical."
            )

            # correct 2025 API call
            completion = client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=250
            )

            explanation = completion.choices[0].message.content.strip()

        st.success(explanation)
