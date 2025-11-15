import streamlit as st
from openai import OpenAI
from lottie_util import display_lottie


def recommender_interface():
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    st.header("🤖 FinWise Recommender")

    display_lottie(
        "https://assets5.lottiefiles.com/packages/lf20_w51pcehl.json",
        height=110,
        key="recommender"
    )

    age = st.number_input("Your age", min_value=18, max_value=100, value=30)

    goal = st.selectbox(
        "Main financial goal",
        ["Retirement", "Buy a House", "Emergency Fund", "Travel", "Education"]
    )

    risk = st.selectbox(
        "Risk Tolerance",
        ["Low", "Medium", "High"]
    )

    if st.button("Recommend for Me"):
        with st.spinner("Analyzing your profile..."):

            prompt = (
                f"I am {age} years old. My main financial goal is '{goal}', "
                f"and my risk tolerance is '{risk}'. "
                "Recommend a personalized investment plan or financial product for me. "
                "Keep the explanation simple and no longer than 3–4 sentences."
            )

            completion = client.chat.completions.create(
                model="gpt-4o-mini",  
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200
            )

            recommendation = completion.choices[0].message.content.strip()

        st.success(recommendation)
