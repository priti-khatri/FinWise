import streamlit as st

def recommender_interface():
    st.title("🎯 Personalized Finance Guide")

    st.markdown("""
        <style>
        .recommendation-box {
            background: linear-gradient(145deg, #f3e5f5, #e8f5e9);
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 4px 10px rgba(0,0,0,0.05);
            margin-top: 20px;
            font-family: 'Poppins', sans-serif;
        }
        </style>
    """, unsafe_allow_html=True)

    st.subheader("Let's get to know you")

    income = st.slider("What's your monthly income (in ₹)?", 0, 200000, 30000, step=5000)
    knowledge = st.selectbox("How would you rate your finance knowledge?", ["Beginner", "Intermediate", "Advanced"])
    goal = st.selectbox("What's your primary financial goal?", ["Saving", "Investing", "Debt Repayment", "Learning Basics", "Building Credit"])

    st.markdown("#### Based on your inputs, here's what we recommend:")

    if st.button("🎯 Show Recommendations"):
        with st.container():
            st.markdown("<div class='recommendation-box'>", unsafe_allow_html=True)

            if knowledge == "Beginner":
                st.write("- 🧠 Start with the glossary to understand basic finance terms.")
                st.write("- 📺 Follow YouTube channels like CA Rachna, Pranjal Kamra, or Finshots.")
                st.write("- 💡 Use a budgeting app to track spending.")
            elif knowledge == "Intermediate":
                st.write("- 📈 Try investing in index funds like Nifty 50 via apps like Zerodha or Groww.")
                st.write("- 💸 Learn about SIPs, insurance, and basic tax-saving tools (ELSS).")
                st.write("- 💼 Start a 3-month emergency fund.")

            if goal == "Saving":
                st.write("- 🚀 Automate 20% of your income into a separate savings account.")
            elif goal == "Investing":
                st.write("- 💹 Consider mutual funds, ETFs, or fractional stocks with low risk.")
            elif goal == "Debt Repayment":
                st.write("- 🧾 Use the ‘avalanche’ method: pay highest interest debts first.")
            elif goal == "Learning Basics":
                st.write("- 📚 Read 'The Psychology of Money' or 'Rich Dad Poor Dad'.")
            elif goal == "Building Credit":
                st.write("- 💳 Get a secured credit card or use a credit builder app like Step or OneCard.")

            if income < 30000:
                st.write("- ⚠️ Focus on savings and cutting fixed expenses first.")
            elif income >= 50000:
                st.write("- ✅ You’re in a great spot to begin SIPs and emergency fund building.")

            st.markdown("</div>", unsafe_allow_html=True)
