import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import os

# --- Setup Halaman ---
st.set_page_config(page_title="Kalkulator Jejak Karbon", page_icon="🌿", layout="centered")

# --- Judul & Deskripsi ---
st.markdown("""
    <div style="text-align:center;">
        <h1 style="color:green;">🌱 Kalkulator Jejak Karbon 🌍</h1>
        <p style="font-size:18px; color:#555;">Hitung jejak karbonmu, simpan kontribusimu, dan bantu analisis bersama komunitas! 🌏✨</p>
    </div>
""", unsafe_allow_html=True)

# --- Fungsi Hitung Karbon ---
def calculate_carbon(transport_km, energy_kwh, food_meat_kg):
    transport_emission = transport_km * 0.2   # kg CO2/km
    energy_emission = energy_kwh * 0.5        # kg CO2/kWh
    food_emission = food_meat_kg * 10         # kg CO2/kg daging
    total = transport_emission + energy_emission + food_emission
    return transport_emission, energy_emission, food_emission, total

# --- Form Input User ---
st.subheader("🔢 Masukkan Data Aktivitasmu")

with st.form("carbon_form"):
    transport_km = st.number_input("🚗 Jarak Transportasi (km/minggu)", min_value=0.0)
    energy_kwh = st.number_input("⚡ Pemakaian Energi (kWh/bulan)", min_value=0.0)
    food_meat_kg = st.number_input("🍖 Konsumsi Daging (kg/minggu)", min_value=0.0)
    country = st.selectbox("🌍 Negara", ["Indonesia", "Malaysia", "Singapura", "Lainnya"])
    submitted = st.form_submit_button("Hitung Jejak Karbon 🌿")

# --- Proses Perhitungan & Penyimpanan ---
if submitted:
    transport_emission, energy_emission, food_emission, total = calculate_carbon(
        transport_km, energy_kwh, food_meat_kg
    )

    # Tampilkan hasil
    st.success(f"🌍 Total Jejak Karbonmu: **{total:.2f} kg CO2/bulan**")
    st.write(f"🚗 Transportasi: {transport_emission:.2f} kg")
    st.write(f"⚡ Energi: {energy_emission:.2f} kg")
    st.write(f"🍖 Makanan: {food_emission:.2f} kg")
    st.caption(f"📅 Dicatat pada: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")

    # Simpan data ke CSV
    new_data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "transport": transport_km,
        "energy": energy_kwh,
        "food": food_meat_kg,
        "total": total,
        "country": country
    }

    df_new = pd.DataFrame([new_data])

    file_path = "data.csv"
    if os.path.exists(file_path):
        df_old = pd.read_csv(file_path)
        df_all = pd.concat([df_old, df_new], ignore_index=True)
    else:
        df_all = df_new

    df_all.to_csv(file_path, index=False)

    st.success("✅ Data berhasil disimpan!")

    # --- Visualisasi ---
    st.markdown("---")
    st.subheader("📊 Visualisasi Jejak Karbon Komunitas")

    st.write("Total jejak karbon per negara:")
    fig = px.bar(df_all, x="country", y="total", color="country", title="Total Emisi CO2 per Negara", height=400)
    st.plotly_chart(fig, use_container_width=True)

    # --- Tabel Semua Data ---
    with st.expander("📄 Lihat Semua Data"):
        st.dataframe(df_all)

