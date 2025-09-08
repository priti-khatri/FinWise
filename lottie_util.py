import requests
from streamlit_lottie import st_lottie

def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

def display_lottie(url, height=250, key=None, speed=1):
    lottie_json = load_lottieurl(url)
    if lottie_json:
        st_lottie(lottie_json, height=height, key=key, speed=speed)