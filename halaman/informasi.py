import streamlit as st

def show():
    if "info_selected" not in st.session_state:
        st.session_state.info_selected = "O3"

    st.markdown("""
        <style>
        .block-container { padding-top: 1rem !important; }
        h1 a, h2 a, h3 a, h4 a { display: none !important; }
        div[data-testid="stButton"] { display:flex; justify-content:center; }
        div[data-testid="stButton"] button {
            width:100%;
            border-radius:10px;
            padding:0.45rem 0.6rem;
            font-weight:600;
            background-color:#b8d5f1;
            color:black;
            border:none;
            transition: all 0.12s ease-in-out;
        }
        div[data-testid="stButton"] button:hover {
            background-color: #90c2f1 !important;
        }
        .info-active-default {
            background-color: #5b8ef0 !important;
            color: white !important;
            font-weight:700 !important;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1 style='text-align:center;'>Informasi</h1><hr>", unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])

    info_buttons = [
        ("O3", "O₃"),
        ("CO", "CO"),
        ("SO2", "SO₂"),
        ("NO2", "NO₂"),
        ("Metode", "Metode"),
    ]

    with col1:
        for key, label in info_buttons:
            if st.button(label, key=f"info_btn_{key}"):
                st.session_state.info_selected = key

        selected_key = st.session_state.get("info_selected", "O3")
        label_map = {k: v for k, v in info_buttons}
        selected_label = label_map.get(selected_key, "O₃")

        st.markdown(
            f"""
            <style>
            button[aria-label="{selected_label}"] {{
                background-color: #5b8ef0 !important;
                color: white !important;
                font-weight: 700 !important;
            }}
            button[aria-label="{selected_label}"]:hover {{
                background-color: #4a7be0 !important;
            }}
            </style>
            """,
            unsafe_allow_html=True
        )

    with col2:
        st.markdown("### Penjelasan:")
        sel = st.session_state.info_selected

        if sel == "O3":
            st.subheader("O₃ (Ozon Troposfer)")
            st.write("""
            **Deskripsi singkat:**  
            Ozon troposfer (O₃) merupakan polutan sekunder yang terbentuk melalui reaksi fotokimia antara nitrogen oksida (NOx) dan senyawa organik volatil (VOC) di bawah sinar matahari.
            """)
            st.write("**Sumber utama:**")
            st.write("- Emisi kendaraan bermotor, pembangkit listrik, dan industri.")
            st.write("- VOC dari pelarut, bahan bakar, dan aktivitas biologis.")
            st.write("**Dampak kesehatan dan lingkungan:**")
            st.write("- Mengiritasi saluran pernapasan dan memperburuk penyakit paru.")
            st.write("- Merusak vegetasi dan menurunkan hasil pertanian.")

        elif sel == "CO":
            st.subheader("CO (Karbon Monoksida)")
            st.write("""
            **Deskripsi singkat:**  
            Karbon monoksida (CO) adalah gas tidak berwarna dan tidak berbau yang dihasilkan dari pembakaran tidak sempurna bahan bakar karbon.
            """)
            st.write("**Sumber utama:**")
            st.write("- Kendaraan bermotor (terutama mesin bensin).")
            st.write("- Pembakaran biomassa dan bahan bakar fosil.")
            st.write("**Dampak kesehatan:**")
            st.write("- Mengikat hemoglobin lebih kuat dari oksigen → menghambat suplai oksigen ke tubuh.")
            st.write("- Paparan tinggi dapat menyebabkan pusing, mual, hingga kematian.")

        elif sel == "SO2":
            st.subheader("SO₂ (Sulfur Dioksida)")
            st.write("""
            **Deskripsi singkat:**  
            Sulfur dioksida (SO₂) adalah gas asam yang dihasilkan dari pembakaran bahan bakar yang mengandung sulfur.
            """)
            st.write("**Sumber utama:**")
            st.write("- Pembangkit listrik berbahan batu bara atau minyak berat.")
            st.write("- Aktivitas industri seperti pengolahan logam dan pembuatan semen.")
            st.write("**Dampak kesehatan dan lingkungan:**")
            st.write("- Menyebabkan iritasi tenggorokan dan bronkospasme.")
            st.write("- Berkontribusi terhadap pembentukan hujan asam dan kabut.")

        elif sel == "NO2":
            st.subheader("NO₂ (Nitrogen Dioksida)")
            st.write("""
            **Deskripsi singkat:**  
            NO₂ adalah gas berwarna coklat kemerahan yang dihasilkan dari pembakaran suhu tinggi dan merupakan prekursor ozon troposfer.
            """)
            st.write("**Sumber utama:**")
            st.write("- Emisi kendaraan bermotor (terutama diesel).")
            st.write("- Pembangkit listrik dan pembakaran industri.")
            st.write("**Dampak kesehatan dan lingkungan:**")
            st.write("- Menyebabkan iritasi saluran napas dan menurunkan fungsi paru-paru.")
            st.write("- Berperan dalam pembentukan partikel halus (PM2.5) dan ozon permukaan.")

        elif sel == "Metode":
            st.subheader("Metode Klasifikasi — Support Vector Machine (SVM)")
            st.write("""
            **Ringkasan:**  
            Support Vector Machine (SVM) adalah algoritma supervised learning untuk menemukan hyperplane terbaik yang memisahkan kelas data.  
            Perancangan ini menggunakan **dua kernel utama: Linear dan RBF (Radial Basis Function)**.
            """)
            st.write("**Kernel Linear:**")
            st.write("- Cocok jika data relatif linier terpisah di ruang fitur.")
            st.write("- Cepat dan mudah diinterpretasi, hanya butuh parameter regulasi (C).")
            st.write("**Kernel RBF:**")
            st.write("- Mampu memisahkan data non-linear dengan memetakan ke ruang berdimensi tinggi.")
            st.write("- Perlu tuning parameter `C` dan `gamma` agar tidak overfitting.")