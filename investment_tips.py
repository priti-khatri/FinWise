import streamlit as st
import openai
import utils

def investment_tips_interface():
    st.title("📈 Personalized Investment Tips")

    openai.api_key = st.secrets["openai_api_key"]

    risk_tolerance = st.selectbox("Your risk tolerance level", ["Low", "Medium", "High"])
    age = st.number_input("Your age", min_value=13, max_value=100, value=22)

    prompt = f"""
    Provide investment tips suitable for a {age} years old GenZ with {risk_tolerance} risk tolerance.
    """

    if st.button("Get Tips"):
        with st.spinner("Generating tips..."):
            tips = utils.get_openai_response([{"role": "user", "content": prompt}])
        st.markdown(tips)
