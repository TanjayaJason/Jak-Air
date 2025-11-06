import streamlit as st

def show():
    st.markdown("""
        <style>
        .block-container { padding-top: 1rem !important; }
        .stMarkdown h1 a, .stMarkdown h2 a, .stMarkdown h4 a { display: none; }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("""
        <h1 style="text-align:center;">
            Sistem Klasifikasi Kualitas Udara dengan Data Sentinel-5P <em>(Jak Air)</em>
        </h1>
        <hr>
        <h4 style="color:#1f4e79;">Deskripsi Singkat</h4>
        <p style="text-align:justify; font-size:16px;">
            Aplikasi ini dirancang untuk memantau dan mengklasifikasikan kualitas udara di wilayah DKI Jakarta menggunakan data satelit Sentinel-5P. 
            Melalui integrasi teknologi penginderaan jauh dan <em>machine learning</em>, aplikasi ini memanfaatkan algoritma <em>Support Vector Machine (SVM)</em> dengan dua jenis kernel, yaitu 
            Linear dan <em>Radial Basis Function (RBF)</em>, untuk menentukan kategori kualitas udara secara keseluruhan di DKI Jakarta.<br>
            Selain menampilkan peta sebaran polutan, aplikasi ini juga menyediakan menu pelatihan dan pengujian model secara mandiri. 
            Pengguna dapat mengunggah dataset, melakukan eksperimen parameter, melatih model SVM, dan langsung menguji hasil prediksinya melalui antarmuka web yang interaktif dan mudah digunakan. 
            Sistem ini diharapkan dapat membantu pengguna memahami kondisi udara dan melakukan analisis secara cepat, fleksibel, dan informatif.
        </p>
    """, unsafe_allow_html=True)

    st.info("Gunakan menu di sidebar untuk berpindah antar modul.")