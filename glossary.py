# glossary.py

import streamlit as st
import json
import os

def load_terms():
    file_path = os.path.join("data", "finance_terms.json")
    with open(file_path, "r") as f:
        return json.load(f)

def glossary_interface():
    st.subheader("📖 Financial Glossary")
    st.markdown("Explore financial terms in a simple, Gen Z–friendly way. Use the search box to find what you need.")

    search = st.text_input("🔍 Search for a term")

    terms = load_terms()

    if search:
        results = {k: v for k, v in terms.items() if search.lower() in k.lower()}
        if results:
            for term, definition in results.items():
                with st.expander(f"📘 {term}"):
                    st.markdown(definition)
        else:
            st.warning("No matching term found.")
    else:
        for term, definition in terms.items():
            with st.expander(f"📘 {term}"):
                st.markdown(definition)
