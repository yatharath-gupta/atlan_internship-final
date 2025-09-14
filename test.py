import streamlit as st

keys = st.secrets["GEMINI_API_KEYS"]

st.write("Loaded keys:", keys)   # just to verify locally
