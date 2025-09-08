import streamlit as st
import openai
import utils

def explainer_interface():
    st.title("💡 Explain Complex Finance Concepts")

    openai.api_key = st.secrets["openai_api_key"]

    concept = st.text_input("Enter a finance concept you want explained:")

    if st.button("Explain"):
        if concept.strip():
            prompt = f"Explain the following finance concept in a simple way for GenZ: {concept}"
            with st.spinner("Generating explanation..."):
                explanation = utils.get_openai_response([{"role": "user", "content": prompt}])
            st.markdown(explanation)
        else:
            st.warning("Please enter a finance concept.")
