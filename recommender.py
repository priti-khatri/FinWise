import streamlit as st
import openai
import utils

def recommender_interface():
    st.title("🎯 Personalized Finance Recommender")

    openai.api_key = st.secrets["openai_api_key"]

    income = st.slider("Your monthly income (USD)", 0, 20000, 3000)
    knowledge_level = st.selectbox("Your finance knowledge level", ["Beginner", "Intermediate", "Advanced"])

    prompt = f"""
    Recommend next best steps for a GenZ user with a monthly income of ${income} and finance knowledge level: {knowledge_level}.
    Provide simple, actionable advice on investments, savings, and learning.
    """

    if st.button("Get Recommendations"):
        with st.spinner("Fetching personalized recommendations..."):
            response = utils.get_openai_response([{"role": "user", "content": prompt}])
        st.markdown(response)
