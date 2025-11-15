import streamlit as st
from openai import OpenAI
from lottie_util import display_lottie


def investment_tips_interface():

    client = OpenAI(api_key=st.secrets["OPENAI_API_KEY"])

    st.header("💡 FinWise Investment Tips")

    display_lottie(
        "https://assets5.lottiefiles.com/packages/lf20_2KCXQ7.json",
        height=110,
        key="tips-lottie"
    )

    if st.button("Get Investment Tip"):
        with st.spinner("Fetching tip..."):

            prompt = (
                "Provide a practical investment tip suitable for an average person. "
                "Keep it simple and no longer than 2-3 sentences."
            )

            # API call
            completion = client.chat.completions.create(
                model="gpt-4o-mini",      # recommended: fast + inexpensive
                messages=[{"role": "user", "content": prompt}],
                max_tokens=120
            )

            tip = completion.choices[0].message.content.strip()

        st.success(tip)
