import streamlit as st
from lottie_util import display_lottie

def glossary_interface():
    st.markdown(
        """
        <div class="glass-card">
            <h2 style='color:#f72585;font-size:2.2em;letter-spacing:1px;'>
                📚 Explore Finance Terms
            </h2>
            <p style='font-size:1.16em;'>Swipe through financial lingo and level up your money game! 🤑</p>
        </div>
        """, unsafe_allow_html=True
    )
    display_lottie("https://assets3.lottiefiles.com/packages/lf20_mf2zqwwb.json", height=120, key="glossary_lottie")
    terms = {
        "APR": "Annual Percentage Rate, the yearly interest.",
        "ETF": "Exchange Traded Fund, a basket of assets.",
        "Roth IRA": "A retirement savings account with tax perks.",
        "Diversification": "Don't put all your eggs in one basket!",
    }
    choice = st.selectbox("Pick a term to learn more:", list(terms.keys()))
    st.info(terms[choice])