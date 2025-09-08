import streamlit as st
import pandas as pd

def glossary_interface():
    st.title("📖 Finance Glossary")

    st.markdown("""
        <style>
        .dataframe {
            border-radius: 10px;
            overflow: hidden;
            font-family: 'Poppins', sans-serif;
        }
        .stDataFrame {
            background-color: #f9f9f9;
            border: 1px solid #ccc;
        }
        </style>
    """, unsafe_allow_html=True)

    # Sample glossary data (you can expand this)
    data = [
        {"Term": "Asset", "Definition": "A resource with economic value owned by an individual or organization."},
        {"Term": "Bond", "Definition": "A fixed income instrument that represents a loan made by an investor to a borrower."},
        {"Term": "Credit Score", "Definition": "A number representing the creditworthiness of a person."},
        {"Term": "ETF", "Definition": "Exchange-Traded Fund — a collection of securities traded like a stock."},
        {"Term": "Inflation", "Definition": "The rate at which the general level of prices for goods and services rises."},
        {"Term": "Liability", "Definition": "Something a person or company owes, usually a sum of money."},
        {"Term": "Net Worth", "Definition": "Assets minus liabilities — a snapshot of an individual’s financial health."},
        {"Term": "Yield", "Definition": "The earnings generated and realized on an investment over a particular period."},
    ]
    df = pd.DataFrame(data)

    search_term = st.text_input("Search financial terms (e.g. ETF, asset, yield):").lower()

    if search_term:
        filtered_df = df[df['Term'].str.lower().str.contains(search_term)]
    else:
        filtered_df = df

    st.dataframe(filtered_df, use_container_width=True)
