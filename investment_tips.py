import streamlit as st
import openai
from lottie_util import display_lottie

def investment_tips_interface():
    client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    st.header("💡 FinWise Investment Tips")
    display_lottie("https://assets5.lottiefiles.com/packages/lf20_2KCXQ7.json", height=110, key="tips-lottie")
    if st.button("Get Investment Tip"):
        with st.spinner("Fetching tip..."):
            prompt = "Give me a practical investment tip for an average person, in 2-3 sentences."
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=120,
            )
            tip = response.choices[0].message.content.strip()
            st.success(tip)