import streamlit as st
from lottie_util import display_lottie
import plotly.graph_objs as go

def scenario_interface():
    st.markdown(
        """
        <div class="glass-card">
            <h2 style='color:#3a0ca3;font-size:2.2em;letter-spacing:1px;'>
                📊 Scenario Simulator
            </h2>
            <p style='font-size:1.16em;'>See what happens with your financial choices. It's like choose-your-own-adventure, but for money! 🎲</p>
        </div>
        """, unsafe_allow_html=True
    )
    display_lottie("https://assets1.lottiefiles.com/packages/lf20_oyhfjq9b.json", height=120, key="scenario_lottie")
    invest = st.slider("How much do you want to invest?", 100, 10000, 500)
    years = st.slider("For how many years?", 1, 30, 5)
    rate = st.slider("Expected annual return (%)", 2, 20, 8)
    if st.button("Simulate"):
        progression = [invest * ((1 + rate/100) ** y) for y in range(0, years+1)]
        st.success(f"If you invest ${invest} for {years} years at {rate}%: <br>You'll have **${progression[-1]:,.2f}**", icon="💸")
        fig = go.Figure(
            data=[go.Scatter(x=list(range(0,years+1)), y=progression, mode='lines+markers', line=dict(color='#f72585', width=4))],
            layout=go.Layout(
                title="Investment Growth Over Time",
                xaxis=dict(title="Years"),
                yaxis=dict(title="Portfolio Value ($)", tickprefix="$"),
                template='plotly_dark' if st.session_state.get("dark") else 'plotly_white',
                transition=dict(duration=500)
            )
        )
        st.plotly_chart(fig, use_container_width=True)