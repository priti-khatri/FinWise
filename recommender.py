import streamlit as st

def recommender_interface():
    st.markdown("<div style='background: rgba(0,0,0,0.5); border-radius: 15px; padding: 2rem;'>", unsafe_allow_html=True)
    st.title("🎯 Personalized Finance Recommender")

    income = st.number_input("Enter your monthly income (₹)", min_value=0, step=1000)
    knowledge = st.selectbox("Your finance knowledge level:", ["Beginner", "Intermediate", "Advanced"])

    if st.button("Get Recommendation"):
        if income == 0:
            st.error("Please enter a valid income greater than 0.")
        else:
            recommendation = ""

            if knowledge == "Beginner":
                recommendation = "Start with basic savings and budgeting apps, and learn about mutual funds."
            elif knowledge == "Intermediate":
                recommendation = "Explore SIP investments, ETFs, and diversify your portfolio."
            else:
                recommendation = "Consider advanced stock market strategies and derivatives trading after research."

            st.success(f"Based on your income ₹{income} and knowledge level '{knowledge}', here’s a recommendation: {recommendation}")

    st.markdown("</div>", unsafe_allow_html=True)
