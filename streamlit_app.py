import streamlit as st
import time

# Animasi judul dengan efek ketik
def animated_title(text, delay=0.1):
    placeholder = st.empty()
    current_text = ""
    for char in text:
        current_text += char
        placeholder.title(current_text)
        time.sleep(delay)

# Judul utama dengan animasi ketik
animated_title("Kalkulator Cinta 💖")

# Subjudul biasa
st.title("_Azlina_ sayang :red[Danapati] ❤️")

# Tulisan tambahan
st.write("Ayo berhitung, head over to [docs.streamlit.io](https://docs.streamlit.io/).")

# Tambahan emoji bergerak (secara simulasi)
with st.spinner('Menghitung rasa cinta... 💘'):
    time.sleep(2)

st.success("Cinta 100%! Kamu dan dia cocok banget 😍💯")

# Tambahan select box buat variasi
pilihan = st.selectbox("Menurutmu, cinta itu seperti...", 
                       ["Bunga mekar di musim semi 🌸", 
                        "Teh hangat di sore hari 🍵", 
                        "Sinyal WiFi yang full 📶", 
                        "Kalkulator yang selalu tepat ❤️"])

st.write(f"Kamu memilih: *{pilihan}*")
