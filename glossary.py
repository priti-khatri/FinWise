import streamlit as st

def glossary_interface():
    st.markdown("<div style='background: rgba(0,0,0,0.5); border-radius: 15px; padding: 2rem;'>", unsafe_allow_html=True)
    st.markdown("<h2 style='color:#FFD700;'>📖 Finance Glossary</h2>", unsafe_allow_html=True)

    glossary_data = {
        "Equity": "Ownership in a company represented by shares.",
        "Bond": "A fixed income instrument representing a loan.",
        "ETF": "Exchange-Traded Fund, a basket of securities traded like stocks.",
        "Dividend": "A distribution of profits to shareholders.",
        "IPO": "Initial Public Offering, the first sale of stock by a private company to the public.",
        "Liquidity": "How easily an asset can be converted into cash.",
        "Bull Market": "A market condition where prices are rising or expected to rise.",
        "Bear Market": "A market condition where prices are falling or expected to fall."
    }

    term = st.text_input("Search a term:", placeholder="E.g. Equity, Bond, IPO")

    if term:
        result = glossary_data.get(term.strip().title())
        if result:
            st.markdown(f"<div style='color:#00CFFF; font-size:18px;'><b>{term.title()}:</b> {result}</div>", unsafe_allow_html=True)
        else:
            st.warning("Term not found. Try another!")

    st.markdown("</div>", unsafe_allow_html=True)
