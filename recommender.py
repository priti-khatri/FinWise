import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["openai_api_key"])

def recommender_interface():
    st.subheader("📈 Get Personalized Finance Advice")

    with st.container():
        st.markdown('<div class="card-container">', unsafe_allow_html=True)

        income = st.slider("What's your monthly income? 💸", 1000, 200000, 30000, step=1000)
        experience = st.selectbox("How confident are you in managing money?", ["Beginner", "Intermediate", "Pro"])
        
        if st.button("Recommend Strategy"):
            prompt = f"Suggest a financial strategy for someone with a monthly income of {income} INR and experience level: {experience}."
            with st.spinner("Finding the best plan for you... 🔍"):
                try:
                    res = client.responses.create(
                        model="gpt-5-nano",
                        input=prompt,
                        store=False
                    )
                    st.markdown(f'<div class="card">{res.output_text}</div>', unsafe_allow_html=True)
                except Exception as e:
                    st.error(f"Error: {e}")

        st.markdown('</div>', unsafe_allow_html=True)
