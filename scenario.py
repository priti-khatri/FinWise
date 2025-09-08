import streamlit as st
import openai
import utils

def scenario_interface():
    st.title("🔮 Scenario Simulator & Daily Finance Tip")

    openai.api_key = st.secrets["openai_api_key"]

    scenario = st.text_input("Describe a financial scenario you want to simulate:")

    if st.button("Simulate"):
        if scenario.strip():
            prompt = f"Simulate this financial scenario and give advice: {scenario}"
            with st.spinner("Simulating..."):
                advice = utils.get_openai_response([{"role": "user", "content": prompt}])
            st.markdown(advice)
        else:
            st.warning("Please describe a scenario.")
