import streamlit as st
from datetime import datetime

# --- Konfigurasi halaman ---
st.set_page_config(
    page_title="Kalkulator Jejak Karbon",
    page_icon="🌿",
    layout="centered"
)

# --- Tampilan Judul ---
st.markdown(
    """
    <div style="text-align: center; margin-top: 50px;">
        <h1 style="color: #2E8B57;">🌱 Kalkulator Jejak Karbon 🌍</h1>
        <p style="font-size: 20px; color: gray;">Hitung dan kontribusikan data jejak karbonmu untuk masa depan bumi yang lebih hijau 🌏✨</p>
    </div>
    """,
    unsafe_allow_html=True
)

st.write("")  # Spacer kecil

# --- Fungsi Kalkulasi Jejak Karbon ---
def calculate_carbon(transport_km, energy_kwh, food_meat_kg):
    transport_emission = transport_km * 0.2   # 0.2 kg CO2 per km
    energy_emission = energy_kwh * 0.5         # 0.5 kg CO2 per kWh
    food_emission = food_meat_kg * 10          # 10 kg CO2 per kg daging
    total_emission = transport_emission + energy_emission + food_emission
    return transport_emission, energy_emission, food_emission, total_emission

# --- Tombol Mulai ---
start = st.button("🚀 Mulai Hitung Jejak Karbon")

# --- Jika Mulai ditekan ---
if start:
    st.markdown("---")
    st.subheader("Masukkan Data Aktivitasmu")

    # Form Input Data
    with st.form("input_form"):
        transport_km = st.number_input("🚗 Jarak Transportasi (km/minggu)", min_value=0.0, format="%.2f")
        energy_kwh = st.number_input("⚡ Pemakaian Energi Listrik (kWh/bulan)", min_value=0.0, format="%.2f")
        food_meat_kg = st.number_input("🍖 Konsumsi Daging (kg/minggu)", min_value=0.0, format="%.2f")
        submit = st.form_submit_button("Hitung Sekarang")

    # Jika form disubmit
    if submit:
        transport_emission, energy_emission, food_emission, total_emission = calculate_carbon(
            transport_km, energy_kwh, food_meat_kg
        )

        st.markdown("---")
        st.subheader("🌎 Hasil Perhitungan Jejak Karbonmu")
        st.write(f"🚗 Emisi dari Transportasi: **{transport_emission:.2f} kg CO2/bulan**")
        st.write(f"⚡ Emisi dari Energi Listrik: **{energy_emission:.2f} kg CO2/bulan**")
        st.write(f"🍖 Emisi dari Konsumsi Daging: **{food_emission:.2f} kg CO2/bulan**")
        st.success(f"🌍 Total Jejak Karbonmu: **{total_emission:.2f} kg CO2/bulan**")

        st.caption(f"📅 Dicatat pada: {datetime.now().strftime('%d-%m-%Y %H:%M:%S')}")
