import streamlit as st
from openai import OpenAI

client = OpenAI(api_key=st.secrets["openai_api_key"])

# Predefined terms (you can extend this)
GLOSSARY_TERMS = {
    "Equity": "Ownership of assets that may have debts or other liabilities attached to them.",
    "Mutual Fund": "An investment vehicle that pools money from many investors to purchase securities.",
    "Inflation": "The rate at which the general level of prices for goods and services rises.",
    "Diversification": "A risk management strategy that mixes a wide variety of investments within a portfolio.",
    "ETF": "Exchange-Traded Fund, a type of investment fund traded on stock exchanges.",
    "Robo-Advisor": "A digital platform that provides automated, algorithm-driven financial planning services.",
    "Fixed Deposit": "A financial instrument provided by banks which provides investors with a higher interest rate than a regular savings account.",
}

def glossary_interface():
    st.subheader("📚 Finance Glossary")

    st.markdown('<div class="card-container">', unsafe_allow_html=True)

    # Create a select box for glossary terms
    term = st.selectbox("Select a finance term to learn more 👇", list(GLOSSARY_TERMS.keys()) + ["Custom Term"])

    if term != "Custom Term":
        st.markdown(f'<div class="card"><h4>{term}</h4><p>{GLOSSARY_TERMS[term]}</p></div>', unsafe_allow_html=True)
    else:
        user_input = st.text_input("Enter your finance term:")
        if st.button("Explain Term"):
            if user_input:
                with st.spinner("Looking it up... 🔍"):
                    try:
                        response = client.responses.create(
                            model="gpt-5-nano",
                            input=f"Explain the finance term: {user_input}",
                            store=False
                        )
                        st.markdown(f'<div class="card"><h4>{user_input}</h4><p>{response.output_text}</p></div>', unsafe_allow_html=True)
                    except Exception as e:
                        st.error(f"Error: {e}")

    st.markdown('</div>', unsafe_allow_html=True)
