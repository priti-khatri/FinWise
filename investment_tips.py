import streamlit as st
from lottie_util import display_lottie
import random

def investment_tips_interface():
    st.markdown(
        """
        <div class="glass-card">
            <h2 style='color:#4895ef;font-size:2.2em;letter-spacing:1px;'>
                💡 Investment Tips
            </h2>
            <p style='font-size:1.16em;'>Discover smart, actionable tips to grow your wealth! 💸</p>
        </div>
        """, unsafe_allow_html=True
    )
    display_lottie("https://assets2.lottiefiles.com/private_files/lf30_oqpbtola.json", height=140, key="tips_lottie")
    tips = [
        "Start investing early, even with small amounts.",
        "Automate your savings for consistency.",
        "Diversify — spread your investments across different assets.",
        "Don’t try to time the market!",
        "Review your portfolio every 6 months.",
    ]
    st.write("💡 **Tip of the day:**")
    st.info(random.choice(tips))