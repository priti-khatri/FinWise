import streamlit as st
import matplotlib.pyplot as plt

def trend_interface():
    st.markdown("<div style='background: rgba(0,0,0,0.5); border-radius: 15px; padding: 2rem;'>", unsafe_allow_html=True)
    st.title("📊 Market Trends")

    st.markdown("""
        Explore recent financial trends and stock market performance.
    """)

    # Dummy trend data
    months = ['Jan', 'Feb', 'Mar', 'Apr', 'May']
    prices = [100, 120, 115, 130, 125]

    fig, ax = plt.subplots()
    ax.plot(months, prices, marker='o', color='#00CFFF', linewidth=2)
    ax.set_facecolor('none')
    fig.patch.set_alpha(0)  # transparent background

    ax.set_xlabel("Months")
    ax.set_ylabel("Index Price")
    ax.set_title("Sample Stock Market Trend")

    st.pyplot(fig)

    st.markdown("</div>", unsafe_allow_html=True)
