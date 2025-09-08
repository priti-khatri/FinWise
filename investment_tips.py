import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["openai_api_key"])

def investment_tips_interface():
    st.subheader("💡 Smart Investment Tips for You")

    st.markdown('<div class="card-container">', unsafe_allow_html=True)

    age = st.slider("📊 What's your age?", 18, 65, 25)
    risk_appetite = st.selectbox("🧠 Risk Preference", ["Low", "Moderate", "High"])
    goal = st.text_input("🎯 What's your primary financial goal? (e.g., Retirement, Buy a car, Travel)")

    if st.button("Get Tips"):
        if goal:
            with st.spinner("Tailoring advice just for you... ✨"):
                try:
                    prompt = (
                        f"Give smart investment tips for a {age}-year-old with {risk_appetite.lower()} risk appetite, "
                        f"whose goal is: {goal}. Keep it practical and beginner-friendly."
                    )
                    response = client.responses.create(
                        model="gpt-5-nano",
                        input=prompt,
                        store=False
                    )
                    st.markdown(f'<div class="card"><h4>Tips for You</h4><p>{response.output_text}</p></div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error generating tips: {e}")
        else:
            st.warning("Please fill out all fields to get accurate tips.")

    st.markdown('</div>', unsafe_allow_html=True)

