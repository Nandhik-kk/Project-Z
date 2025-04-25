import streamlit as st

# Konfigurasi halaman
st.set_page_config(
    page_title="Kalkulator Jejak Karbon",
    page_icon="🌿",
    layout="centered"
)

# Tampilan Judul
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px;">
        <h1 style="color: #2E8B57;">🌱 Kalkulator Jejak Karbon 🌍</h1>
        <p style="font-size: 20px; color: gray;">Bersama kita jaga bumi untuk generasi masa depan 🌏✨</p>
    </div>
    """,
    unsafe_allow_html=True
)
