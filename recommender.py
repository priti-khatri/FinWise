import streamlit as st
from lottie_util import display_lottie

def recommender_interface():
    st.markdown(
        """
        <div class="glass-card">
            <h2 style='color:#b5179e;font-size:2.2em;letter-spacing:1px;'>
                ✨ Get Personalized Recommendations
            </h2>
            <p style='font-size:1.16em;'>Let us recommend the best financial moves for you! 🌟</p>
        </div>
        """, unsafe_allow_html=True
    )
    display_lottie("https://assets1.lottiefiles.com/packages/lf20_tfb3estd.json", height=130, key="rec_lottie")
    age = st.slider("How old are you?", 16, 60, 22)
    risk = st.select_slider("Choose your risk level:", ["Low", "Medium", "High"], value="Medium")
    if st.button("Get Recommendation"):
        if age < 25 and risk == "High":
            st.success("Consider aggressive growth ETFs and crypto (but DYOR)! 🚀")
        elif risk == "Low":
            st.info("Index funds and high-yield savings are your friends! 💰")
        else:
            st.success("Mix it up! Diversify between stocks and ETFs.")