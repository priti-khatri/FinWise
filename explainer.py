import streamlit as st
from lottie_util import display_lottie

def explainer_interface():
    st.markdown(
        """
        <div class="glass-card">
            <h2 style='color:#7209b7;font-size:2.2em;letter-spacing:1px;'>
                🧠 Explain a Concept
            </h2>
            <p style='font-size:1.16em;'>Confused? Enter a concept and get an easy, GenZ-style breakdown! 🤓</p>
        </div>
        """, unsafe_allow_html=True
    )
    display_lottie("https://assets4.lottiefiles.com/packages/lf20_ysas1bgg.json", height=120, key="explainer_lottie")
    concept = st.text_input("Type any finance term or concept:")
    if st.button("Explain"):
        if concept:
            st.success(f"'{concept}' is a cool money thing! (Add your explainer logic here!)")