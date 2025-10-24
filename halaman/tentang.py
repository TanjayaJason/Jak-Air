import streamlit as st

def show():
    st.markdown("""
        <style>
        .stMarkdown h1 a, .stMarkdown h2 a, .stMarkdown h4 a { display: none; }
        .block-container { padding-top: 0rem !important; }
        h1 { text-align: center; }
        .bio {
            color: #0D1B2A;
            font-size: 1rem;
            line-height: 1.6;
        }
        .bio b { color: #5b8ef0; }
        .section-title {
            font-size: 1.3rem;
            font-weight: 700;
            color: #5b8ef0;
        }
        .latar {
            text-align: justify;
            color: #0D1B2A;
            line-height: 1.7;
            font-size: 1rem;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1>Tentang Pengembang</h1><hr>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2.5])

    with col1:
        st.image("Data/images/foto.png", width=180)

    with col2:
        st.markdown("""
        <div class="bio">
            <p><b>Nama:</b> Tanjaya Jason Winata<br>
            <b>NIM:</b> 535220041<br>
            <b>Email:</b> tanjaya.535220041@stu.untar.ac.id<br>
            <b>Fakultas:</b> Teknologi Informasi<br>
            <b>Program Studi:</b> Teknik Informatika<br>
            <b>Universitas:</b> Tarumanagara</p>
            <b>Dosen Pembimbing:</b>
            <ul>
                <li>Prof. Dr. Ir. Dyah Erny Herwindiati, M.Si.</li>
                <li>Janson Hendryli, S.Kom., M.Kom.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)

    st.markdown("""
        <div class="section-title">Latar Belakang Skripsi</div>
        <div class="latar">
            Perancangan aplikasi ini berangkat dari meningkatnya permasalahan polusi udara di wilayah perkotaan, khususnya DKI Jakarta, yang ditandai oleh tingginya konsentrasi gas pencemar seperti NO₂, SO₂, CO, dan O₃. 
            Sistem pemantauan darat yang tersedia memiliki akurasi tinggi, namun cakupannya masih terbatas, sebarannya belum merata, serta memerlukan biaya operasional yang besar.<br> 
            Sebagai solusi, aplikasi ini memanfaatkan data satelit Sentinel-5P yang bersifat global, terbuka, dan terbarukan, sehingga mampu melengkapi sistem pemantauan konvensional dengan informasi spasial-temporal yang lebih komprehensif. 
            Implementasi algoritma <em>Support Vector Machine (SVM)</em> digunakan untuk mengklasifikasikan kondisi udara berdasarkan parameter gas polutan.<br> 
            Pengembangan aplikasi ini diharapkan dapat menjadi langkah awal menuju sistem pemantauan kualitas udara berbasis penginderaan jauh yang efisien, terbuka, dan adaptif bagi masyarakat serta pengambil kebijakan. 
        </div> 
    """, unsafe_allow_html=True)