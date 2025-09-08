import streamlit as st
import openai
import utils

GLOSSARY = {
    "Equity": "Ownership interest in a company, represented by shares of stock.",
    "Bond": "A fixed income instrument representing a loan made by an investor to a borrower.",
    "IPO": "Initial Public Offering, the first sale of stock by a private company to the public.",
    "Dividend": "A portion of a company's earnings distributed to shareholders.",
    "Liquidity": "The ease with which an asset can be converted into cash without affecting its price.",
    "Yield": "The income return on an investment, usually expressed as a percentage.",
}

def glossary_interface():
    st.title("📖 Finance Glossary")

    term = st.text_input("Search a financial term (e.g., IPO, Equity, Bond):").strip()

    if term:
        definition = GLOSSARY.get(term.capitalize())
        if definition:
            st.markdown(f"**{term.capitalize()}**: {definition}")
        else:
            st.markdown("Term not found. Ask me in the Chatbot!")
