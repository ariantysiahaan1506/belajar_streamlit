import numpy as np
import streamlit as st
import pandas as pd


st.title("Welcome to My Portfolio")
st.write("Hopefully you enjoy to visit this site.")



#SIDEBAR

# Menambahkan judul sidebar
st.sidebar.title("Navigasi")

# Menampilkan radio button dengan banyak pilihan
page = st.sidebar.radio("Pilih Halaman", ["Tentang Saya", "Proyek", "Data Analyst", "Kontak"])



if page == "Tentang Saya":
    import tentang_saya
    tentang_saya.tampilkan_tentang_saya()
elif page == "Kontak":
    import kontak
    kontak.tampilkan_kontak()
elif page == "Proyek":
    import visualisasi
    visualisasi.tampilkan_visualisasi()
elif page == "Data Analyst":
    import prediksi
    prediksi.tampilkan_prediksi()
