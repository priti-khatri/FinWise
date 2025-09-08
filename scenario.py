import streamlit as st
import openai
from lottie_util import display_lottie

def scenario_interface():
    client = openai.OpenAI(api_key=st.secrets["OPENAI_API_KEY"])
    st.header("📊 FinWise Scenario Simulator")
    display_lottie("https://assets2.lottiefiles.com/packages/lf20_b7xv6h5r.json", height=110, key="scenario-lottie")
    scenario = st.text_area("Describe a financial scenario to simulate (e.g., \"If I invest $500/month for 10 years at 7% return...\")")
    if st.button("Simulate"):
        with st.spinner("Simulating..."):
            prompt = f"Analyze this personal finance scenario and provide projected results in 3-5 bullet points: {scenario}"
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=220,
            )
            result = response.choices[0].message.content.strip()
            st.success(result)