# recommender.py

import streamlit as st
import json
import os

def load_recommendations():
    file_path = os.path.join("data", "recommendations.json")
    with open(file_path, "r") as f:
        return json.load(f)

def recommendation_interface():
    st.subheader("🎯 Personalized Finance & Learning Path")

    recommendations = load_recommendations()

    income = st.selectbox(
        "What is your monthly income range? 💵",
        ["Low Income", "Medium Income", "High Income"]
    )

    knowledge = st.selectbox(
        "How would you rate your finance knowledge? 📚",
        ["Beginner", "Intermediate", "Advanced"]
    )

    if st.button("Get Recommendations"):
        advice = recommendations.get(income, {}).get(knowledge, None)
        if advice:
            st.markdown(f"### Here's your personalized advice:")
            st.success(advice)
        else:
            st.error("Sorry, no recommendations found for this selection. Try different options.")
