import streamlit as st
import requests
import matplotlib.pyplot as plt
from datetime import datetime

def trend_interface():
    st.title("📊 Financial Trends & Insights")

    st.markdown("""
        <style>
        .trend-card {
            background-color: #f1f8e9;
            border-radius: 12px;
            padding: 18px;
            margin-bottom: 16px;
            box-shadow: 0 3px 10px rgba(0,0,0,0.08);
            font-family: 'Poppins', sans-serif;
            transition: transform 0.2s;
        }
        .trend-card:hover {
            transform: translateY(-3px);
        }
        .trend-card a {
            text-decoration: none;
            color: #2e7d32;
        }
        .trend-card small {
            color: #555;
        }
        .section-header {
            color: #4caf50;
            font-weight: 700;
        }
        </style>
    """, unsafe_allow_html=True)

    st.subheader("Latest Market Overview")

    # market news
    news_url = "https://financialmodelingprep.com/api/v3/stock_news?limit=5"
    try:
        response = requests.get(news_url)
        response.raise_for_status()
        news = response.json()
        if isinstance(news, list):
            for article in news:
                date_str = article.get('publishedDate', '')[:10]
                try:
                    date_obj = datetime.strptime(date_str, "%Y-%m-%d")
                    date_formatted = date_obj.strftime("%b %d, %Y")
                except:
                    date_formatted = date_str
                st.markdown(f"""
                    <div class="trend-card">
                        <a href="{article.get('url', '#')}" target="_blank">
                            <h4>{article.get('title', 'No title')}</h4>
                        </a>
                        <p>{article.get('site', '')}</p>
                        <small>{date_formatted}</small>
                    </div>
                """, unsafe_allow_html=True)
        else:
            st.warning("No news available at the moment.")
    except Exception as e:
        st.error(f"Couldn't load market news: {e}")

    st.subheader("Nifty 50 Last 7 Days")

    ALPHAVANTAGE_API_KEY = st.secrets.get("ALPHAVANTAGE_API_KEY", None)
    if ALPHAVANTAGE_API_KEY:
        nifty_symbol = "^NSEI"
        url = f"https://www.alphavantage.co/query?function=TIME_SERIES_DAILY&symbol={nifty_symbol}&apikey={ALPHAVANTAGE_API_KEY}"
        try:
            data = requests.get(url).json()
            time_series = data.get("Time Series (Daily)", {})
            if time_series:
                dates = sorted(time_series.keys(), reverse=True)[:7]
                dates.reverse()
                prices = [float(time_series[date]["4. close"]) for date in dates]

                fig, ax = plt.subplots(figsize=(7, 4))
                ax.plot(dates, prices, marker='o', color='#4caf50')
                ax.set_title("Nifty 50 Closing Prices")
                ax.set_xlabel("Date")
                ax.set_ylabel("Price (INR)")
                plt.xticks(rotation=45)
                ax.grid(True)
                fig.tight_layout()
                st.pyplot(fig)
            else:
                st.warning("Nifty data not available.")
        except Exception as e:
            st.error(f"Couldn't load Nifty data: {e}")
    else:
        st.info("Add your Alpha Vantage API key in secrets to see Nifty 50 prices.")
