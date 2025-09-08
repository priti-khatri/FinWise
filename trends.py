# trends.py

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import datetime

def load_sample_stock_data():
    dates = pd.date_range(start="2022-01-01", end="2023-12-31", freq="M")
    prices = [16000, 16200, 15800, 16500, 17000, 17500, 18000, 17800, 18200, 18800, 19000, 19500,
              20000, 19800, 20200, 20800, 21000, 21500, 22000, 22500, 23000, 22800, 23200, 23800]
    return pd.DataFrame({"Date": dates, "Price": prices})

def load_sample_inflation_data():
    years = list(range(2015, 2024))
    inflation = [5.9, 4.5, 3.8, 4.2, 4.8, 6.0, 6.5, 5.1, 5.9]
    return pd.DataFrame({"Year": years, "Inflation (%)": inflation})

def trend_interface():
    st.subheader("📊 Finance Trends Visualization")

    view_option = st.selectbox("Choose a trend to view:", ["📉 Stock Market Trend", "💸 Inflation Trend"])

    if view_option == "📉 Stock Market Trend":
        st.markdown("### Sample Nifty 50 Index (2022–2023)")
        stock_data = load_sample_stock_data()
        fig, ax = plt.subplots()
        ax.plot(stock_data["Date"], stock_data["Price"], marker='o', color="skyblue", linewidth=2)
        ax.set_title("Nifty 50 Index Trend")
        ax.set_xlabel("Date")
        ax.set_ylabel("Index Value")
        ax.grid(True)
        st.pyplot(fig)

    elif view_option == "💸 Inflation Trend":
        st.markdown("### India's Historical Inflation (2015–2023)")
        inflation_data = load_sample_inflation_data()
        fig, ax = plt.subplots()
        ax.bar(inflation_data["Year"], inflation_data["Inflation (%)"], color="salmon")
        ax.set_title("India Inflation Rate")
        ax.set_xlabel("Year")
        ax.set_ylabel("Inflation (%)")
        ax.grid(axis='y')
        st.pyplot(fig)

    st.markdown("---")
    st.markdown("ℹ️ *Data shown here is for demo purposes and not pulled from live financial sources.*")
