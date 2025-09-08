import streamlit as st
import openai
from lottie_util import display_lottie

def recommender_interface():
    openai.api_key = st.secrets["OPENAI_API_KEY"]
    st.header("🤖 FinWise Recommender")
    display_lottie("https://assets5.lottiefiles.com/packages/lf20_w51pcehl.json", height=110, key="recommender")
    age = st.number_input("Your age", min_value=18, max_value=100, value=30)
    goal = st.selectbox("Main financial goal", ["Retirement", "Buy a House", "Emergency Fund", "Travel", "Education"])
    risk = st.selectbox("Risk Tolerance", ["Low", "Medium", "High"])
    if st.button("Recommend for Me"):
        with st.spinner("Analyzing..."):
            prompt = (
                f"I am {age} years old. My main goal is '{goal}'. My risk tolerance is '{risk}'. "
                "Suggest a personalized investment or financial product for me, in 3-4 sentences."
            )
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=200,
            )
            recommendation = response["choices"][0]["message"]["content"].strip()
            st.success(recommendation)