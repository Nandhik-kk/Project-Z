import streamlit as st
import pandas as pd
import plotly.express as px
from datetime import datetime
import os

# --- Setup halaman dengan tema earth tone ---
st.set_page_config(page_title="Kalkulator Jejak Karbon", page_icon="🌿", layout="centered")

earth_bg = """
<style>
body {
    background-color: #F4F1ED;
}
</style>
"""
st.markdown(earth_bg, unsafe_allow_html=True)

st.markdown("""
    <div style="text-align:center; padding:20px;">
        <h1 style="color:#3C6E47;">🌍 Kalkulator Jejak Karbon</h1>
        <p style="font-size:18px; color:#5A5A5A;">
        Hitung jejak karbonmu dan bergabung dalam aksi kolektif 🌱</p>
    </div>
""", unsafe_allow_html=True)

# --- Fungsi Hitung Karbon ---
def calculate_carbon(transport_km, energy_kwh, food_meat_kg):
    transport_emission = transport_km * 0.2
    energy_emission = energy_kwh * 0.5
    food_emission = food_meat_kg * 10
    total = transport_emission + energy_emission + food_emission
    return transport_emission, energy_emission, food_emission, total

# --- Form Input ---
st.subheader("📝 Input Aktivitasmu")

with st.form("carbon_form"):
    transport_km = st.number_input("🚗 Jarak Transportasi (km/minggu)", min_value=0.0)
    energy_kwh = st.number_input("⚡ Pemakaian Energi (kWh/bulan)", min_value=0.0)
    food_meat_kg = st.number_input("🍖 Konsumsi Daging (kg/minggu)", min_value=0.0)
    country = st.selectbox("🌍 Negara", ["Indonesia", "Malaysia", "Singapura", "Lainnya"])
    submitted = st.form_submit_button("Hitung Jejak Karbon 🌿")

# --- Proses Perhitungan ---
if submitted:
    transport_emission, energy_emission, food_emission, total = calculate_carbon(
        transport_km, energy_kwh, food_meat_kg
    )

    st.success(f"🌿 Jejak karbonmu: **{total:.2f} kg CO2/bulan**")
    st.write(f"🚗 Transportasi: {transport_emission:.2f} kg")
    st.write(f"⚡ Energi: {energy_emission:.2f} kg")
    st.write(f"🍖 Makanan: {food_emission:.2f} kg")

    # Saran Pengurangan
    st.markdown("### 💡 Tips Mengurangi Jejak Karbon")
    if transport_emission > 50:
        st.write("- Gunakan transportasi umum atau sepeda 🚴‍♂️")
    if energy_emission > 100:
        st.write("- Gunakan lampu hemat energi dan matikan alat saat tidak dipakai 🔌")
    if food_emission > 50:
        st.write("- Kurangi konsumsi daging, ganti sebagian dengan sayur atau sumber protein lain 🥦")

    # Simpan data
    data = {
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "transport": transport_km,
        "energy": energy_kwh,
        "food": food_meat_kg,
        "total": total,
        "country": country
    }
    df_new = pd.DataFrame([data])

    file_path = "data.csv"
    if os.path.exists(file_path):
        df_old = pd.read_csv(file_path)
        df_all = pd.concat([df_old, df_new], ignore_index=True)
    else:
        df_all = df_new
    df_all.to_csv(file_path, index=False)

    # Visualisasi Agregat
    st.markdown("---")
    st.subheader("📊 Jejak Karbon Komunitas")

    fig = px.bar(df_all, x="country", y="total", color="country",
                 title="Total Emisi CO2 per Negara", height=400)
    st.plotly_chart(fig, use_container_width=True)

    # Leaderboard
    st.markdown("### 🏆 Top 5 Kontributor Terhemat")
    top5 = df_all.sort_values(by="total").head(5)[["country", "total", "timestamp"]]
    st.table(top5)

    # Ekspansi Data Lengkap
    with st.expander("📄 Semua Data"):
        st.dataframe(df_all)

