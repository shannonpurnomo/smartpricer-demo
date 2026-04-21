import streamlit as st

# Baca file HTML
with open("smartpricer_final.html", "r", encoding="utf-8") as f:
    html_content = f.read()

# Tampilkan di Streamlit
st.components.v1.html(html_content, height=800, scrolling=True)