import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["openai_api_key"])

def scenario_interface():
    st.subheader("🔮 Finance Scenario Simulator")

    with st.container():
        st.markdown('<div class="card-container">', unsafe_allow_html=True)

        scenario = st.text_input("Enter a 'What if' scenario (e.g., What if I invest ₹10,000 in mutual funds?)")
        if st.button("Simulate"):
            if scenario:
                with st.spinner("Simulating future 📊"):
                    try:
                        res = client.responses.create(
                            model="gpt-5-nano",
                            input=scenario,
                            store=False
                        )
                        st.markdown(f'<div class="card">{res.output_text}</div>', unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"Simulation failed: {e}")
        st.markdown('</div>', unsafe_allow_html=True)
