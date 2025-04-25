import streamlit as st
from github import Github

# Koneksi ke GitHub
g = Github(st.secrets["GITHUB_TOKEN"])
repo = g.get_repo("username/repo-lingkungan")

# Ambil data polusi dari repo
def load_pollution_data():
    contents = repo.get_contents("data/polution.csv")
    return pd.read_csv(contents.download_url)

# Tampilkan peta
st.map(load_pollution_data())

# Form laporan lingkungan
with st.form("laporan"):
    issue = st.text_input("Deskripsi Masalah")
    if st.form_submit_button("Submit"):
        repo.create_issue(title=issue, labels=["environment"])
