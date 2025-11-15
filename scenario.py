import streamlit as st
from openai import OpenAI
from lottie_util import display_lottie

def scenario_interface():
    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    st.header("📊 FinWise Scenario Simulator")

    display_lottie(
        "https://assets2.lottiefiles.com/packages/lf20_b7xv6h5r.json",
        height=110,
        key="scenario-lottie"
    )

    scenario = st.text_area(
        "Describe a financial scenario to simulate (e.g., \"If I invest $500/month for 10 years at 7% return...\")"
    )

    if st.button("Simulate") and scenario.strip():
        with st.spinner("Simulating..."):
            prompt = (
                f"Analyze this personal finance scenario and provide projected results "
                f"in 3-5 bullet points: {scenario}"
            )

            try:
                completion = client.chat.completions.create(
                    model="gpt-4o-mini",  
                    messages=[{"role": "user", "content": prompt}],
                    max_tokens=220
                )

                result = completion.choices[0].message.content.strip()
                st.success(result)

            except Exception as e:
                st.error(f"⚠️ Error during simulation: {str(e)}")
