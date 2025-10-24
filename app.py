import streamlit as st
from halaman import home, pelatihan_pengujian, hasil, informasi, panduan, tentang

# ---------------------- KONFIGURASI DASAR ----------------------
st.set_page_config(
    page_title="Sistem Klasifikasi Kualitas Udara",
    page_icon="🍃",
    layout="wide"
)

# ---------------------- INISIALISASI SESSION STATE ----------------------
if "page" not in st.session_state:
    st.session_state.page = "🏠 Halaman Utama"

def set_page(name):
    st.session_state.page = name
    st.rerun()

# ---------------------- STYLING SIDEBAR ----------------------
st.markdown("""
    <style>
    /* Tombol dasar sidebar */
    [data-testid="stSidebar"] button[kind="secondary"] {
        width: 100%;
        border-radius: 20px;
        font-weight: 600;
        margin: 6px 0;
        border: none;
        transition: all 0.2s ease-in-out;
        background-color: #b5d3f3 !important;
        color: black !important;
        height: 40px; /* biar tinggi konsisten */
    }

    [data-testid="stSidebar"] button[kind="secondary"]:hover {
        background-color: #90c2f1 !important;
        transform: scale(1.02);
    }

    /* Tombol aktif */
    [data-testid="stSidebar"] button[kind="secondary"].active {
        background-color: #6ea8fe !important;
        color: white !important;
        border-radius: 20px !important;
        height: 40px !important;
        box-shadow: 0 0 6px rgba(0,0,0,0.2);
        transform: none !important;
    }
    </style>
""", unsafe_allow_html=True)

# ---------------------- SIDEBAR NAVIGASI ----------------------
st.sidebar.markdown("<h2 style='text-align:center;'>Jak Air</h2>", unsafe_allow_html=True)
st.sidebar.markdown("---")

pages = {
    "🏠 Halaman Utama": "Halaman Utama",
    "📊 Pelatihan & Pengujian": "Pelatihan & Pengujian",
    "ℹ️ Informasi": "Informasi",
    "📘 Panduan": "Panduan",
    "👨‍💻 Tentang Pengembang": "Tentang Pengembang"
}

# Render tombol navigasi
for key, label in pages.items():
    # deteksi aktif
    is_active = (st.session_state.page == key) or (
        st.session_state.page == "📊 Hasil" and key == "📊 Pelatihan & Pengujian"
    )

    # pakai class CSS aktif
    active_class = "active" if is_active else ""
    st.sidebar.markdown(
        f"""
        <style>
        div[data-testid="{key}"] button {{ all: unset; }}
        </style>
        """, unsafe_allow_html=True
    )

    if is_active:
        st.sidebar.markdown(
            f'<button class="active" kind="secondary">{label}</button>',
            unsafe_allow_html=True
        )
    else:
        if st.sidebar.button(label, key=key, use_container_width=True):
            set_page(key)

# ---------------------- PEMANGGIL HALAMAN ----------------------
if st.session_state.page == "🏠 Halaman Utama":
    home.show()
elif st.session_state.page == "📊 Pelatihan & Pengujian":
    pelatihan_pengujian.show()
elif st.session_state.page == "📊 Hasil":
    hasil.show()
elif st.session_state.page == "ℹ️ Informasi":
    informasi.show()
elif st.session_state.page == "📘 Panduan":
    panduan.show()
elif st.session_state.page == "👨‍💻 Tentang Pengembang":
    tentang.show()