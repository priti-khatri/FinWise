import streamlit as st

def load_css():
    with open("styles.css") as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Page config and CSS
st.set_page_config(page_title="FinWise Demo", layout="wide", page_icon="💸")
load_css()

# Dark mode toggle in session_state
if "dark" not in st.session_state:
    st.session_state["dark"] = False

# Toggle button
if st.button("Toggle Dark Mode"):
    st.session_state["dark"] = not st.session_state["dark"]

# Inject dark/light mode CSS
if st.session_state["dark"]:
    st.markdown("<style>body { background: #181926 !important; color: #e0e0e0 !important; } .glass-card { background: rgba(30,30,40,0.7) !important; color: #fff !important; } </style>", unsafe_allow_html=True)
else:
    st.markdown("<style>body { background: #f1f3f6 !important; color: #222 !important; } .glass-card { background: rgba(255,255,255,0.6) !important; color: #222 !important; } </style>", unsafe_allow_html=True)

# Side-by-side layout
col1, col2 = st.columns(2)
with col1:
    st.markdown("""
    <div class="glass-card">
        <h2>Card 1</h2>
        <p>This is the left card. Add a Lottie animation or image here.</p>
        <img src="https://assets10.lottiefiles.com/packages/lf20_tutvdkg0.json" width="100%">
    </div>
    """, unsafe_allow_html=True)
with col2:
    st.markdown("""
    <div class="glass-card">
        <h2>Card 2</h2>
        <p>This is the right card. Add a Lottie animation or image here.</p>
        <img src="https://assets2.lottiefiles.com/private_files/lf30_oqpbtola.json" width="100%">
    </div>
    """, unsafe_allow_html=True)

st.write("This is a minimal test. If you see two glassy cards side by side and the background/dark mode toggle works, your CSS and layout are fixed.")
