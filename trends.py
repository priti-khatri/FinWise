import streamlit as st
import requests
import datetime
import matplotlib.pyplot as plt

def trend_interface():
    st.title("📊 Financial Trends & Insights")

    st.markdown("""
        <style>
        .trend-card {
            background-color: #e8f5e9;
            border-radius: 15px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 12px rgba(0,0,0,0.1);
            font-family: 'Poppins', sans-serif;
        }
        .section-header {
            color: #4caf50;
            font-weight: 700;
        }
        </style>
    """, unsafe_allow_html=True)

    st.subheader("Latest Market Overview")

    # Fetch market news from Financial Modeling Prep API (free tier, no API key needed)
    news_url = "https://financialmodelingprep.com/api/v3/stock_news?limit=5"
    try:
        response = requests.get(news_url)
        news = response.json()
        for article in news:
            st.markdown(f"""
                <div class="trend-card">
                    <a href="{article['url']}" target="_blank" style="text-decoration:none;color:#2e7d32;">
                        <h4>{article['title']}</h4>
                    </a>
                    <p>{article['site']}</p>
                    <small>{article['publishedDate'][:10]}</small>
                </div>
            """, unsafe_allow_html=True)
    except Exception as e:
        st.error("Couldn't load market news.")

    st.subheader("Nifty 50 Last 7 Days")

    # Fetch Nifty 50 prices from Alpha Vantage (free API, requires API key)
    ALPHAVANTAGE_API_KEY = st.secrets.get("ALPHAVANTAGE_API_KEY", None)
    if ALPHAVANTAGE_API_KEY:
        nifty_symbol = "^NSEI"
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={nifty_symbol}&apikey={ALPHAVANTAGE_API_KEY}"
        try:
            data = requests.get(url).json()
            time_series = data.get("Time Series (Daily)", {})
            dates = sorted(time_series.keys(), reverse=True)[:7]
            dates.reverse()
            prices = [float(time_series[date]["4. close"]) for date in dates]

            fig, ax = plt.subplots()
            ax.plot(dates, prices, marker='o', color='#4caf50')
            ax.set_title("Nifty 50 Closing Prices")
            ax.set_xlabel("Date")
            ax.set_ylabel("Price (INR)")
            ax.grid(True)

            st.pyplot(fig)
        except Exception as e:
            st.error("Couldn't load Nifty data.")
    else:
        st.info("Add your Alpha Vantage API key in secrets to see Nifty 50 prices.")

