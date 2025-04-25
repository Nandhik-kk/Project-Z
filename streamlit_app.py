import streamlit as st
import requests
from streamlit_lottie import st_lottie

st.set_page_config(page_title="Kalkulator Jejak Karbon", page_icon="🌿", layout="centered")

# Fungsi untuk load animasi dari URL
def load_lottieurl(url: str):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()

# Load animasi dari LottieFiles
lottie_earth = load_lottieurl("https://assets10.lottiefiles.com/packages/lf20_v7OZCYkF7T.json")

# Tampilan judul utama
st.markdown(
    """
    <h1 style='text-align: center; color: #2E8B57;'>🌱 Kalkulator Jejak Karbon 🌍</h1>
    <p style='text-align: center; font-size: 18px; color: gray;'>
        Hitung dan kontribusikan data jejak karbonmu untuk masa depan bumi yang lebih hijau 🌿✨
    </p>
    """, unsafe_allow_html=True
)

# Tampilkan animasi
with st.container():
    st_lottie(lottie_earth, height=300, key="earth")

# Section pembuka
with st.expander("💡 Apa itu Kalkulator Jejak Karbon?"):
    st.markdown(
        """
        Aplikasi ini membantumu menghitung estimasi **emisi karbon** dari aktivitas sehari-hari seperti transportasi, penggunaan listrik, dan konsumsi daging.

        Data yang kamu masukkan juga akan membantu komunitas dalam melakukan analisis jejak karbon secara kolektif.

        Yuk, mulai menghitung dan jadi bagian dari solusi perubahan iklim! 🌏
        """
    )

# Tombol untuk lanjut
if st.button("Mulai Hitung Sekarang 🚀"):
    st.success("Silakan lanjut ke bagian input data 👇 (belum dibuat di tahap ini)")
