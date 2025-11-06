import streamlit as st

def show():
    st.markdown("""
        <style> 
            .block-container { padding-top: 1rem !important; } 
            h1 { text-align: center !important; } 
            .stMarkdown h1 a, .stMarkdown h2 a, .stMarkdown h4 a { display: none; }
            .panduan {
                text-align: justify;
                color: #0D1B2A;
                line-height: 1.7;
                font-size: 1rem;
            }
            .langkah { margin-bottom: 1.5rem; }
            .langkah-title {
                font-size: 1.15rem;
                font-weight: 700;
                color: #2E8BC0;
                margin-bottom: 0.4rem;
                display: block;
            }
            .panduan-container {
                border: 1px solid #e6e6e6;
                border-radius: 10px;
                padding: 14px 18px;
                margin-bottom: 14px;
                background-color: #ffffff;
                box-shadow: 0 2px 6px rgba(0,0,0,0.06);
            }
            .panduan-title {
                font-size: 1.1rem;
                font-weight: 700;
                color: #2E8BC0;
                margin-bottom: 6px;
            }
            .panduan-desc {
                text-align: justify;
                line-height: 1.65;
                font-size: 0.95rem;
                color: #0D1B2A;
            }
        </style>
    """, unsafe_allow_html=True)

    # ===================== JUDUL =====================
    st.markdown("<h1>Panduan</h1><hr>", unsafe_allow_html=True)

    # ===================== ISI PANDUAN =====================
    st.markdown("""
        <div class="panduan-desc"> 
            Halaman ini berisi penjelasan singkat mengenai fungsi setiap modul pada aplikasi <b>JakAir</b>. 
            Panduan berikut dapat membantu Anda menelusuri fitur yang tersedia secara berurutan dan efektif.
        </div><br>

        <div class="panduan-container">
            <div class="panduan-title">1. Halaman Utama</div>
            <div class="panduan-desc">
                Menampilkan <b>judul dan deskripsi singkat</b> mengenai tujuan aplikasi, yaitu 
                klasifikasi kualitas udara berbasis data satelit Sentinel-5P menggunakan algoritma <i>Support Vector Machine (SVM)</i>. 
                Halaman ini menjadi pengantar sebelum masuk ke fitur utama.
            </div>
        </div>

        <div class="panduan-container">
            <div class="panduan-title">2. Pelatihan & Pengujian Model</div>
            <div class="panduan-desc">
                Pada modul ini, pengguna dapat <b>melatih model SVM secara mandiri</b> dengan mengunggah dataset, 
                mengatur parameter (C dan gamma), dan memilih model terbaik. 
                Setelah model berhasil dilatih, pengguna dapat <b>melakukan pengujian</b> menggunakan data baru untuk memperoleh hasil klasifikasi.
            </div>
        </div>

        <div class="panduan-container">
            <div class="panduan-title">3. Hasil</div>
            <div class="panduan-desc">
                Merupakan lanjutan dari proses pengujian. Halaman ini menampilkan <b>hasil klasifikasi</b> dari model yang telah dibuat, 
                dilengkapi dengan <b>visualisasi peta</b> dan <b>grafik batang</b> untuk memberikan gambaran persebaran dan nilai polutan.
            </div>
        </div>

        <div class="panduan-container">
            <div class="panduan-title">4. Informasi</div>
            <div class="panduan-desc">
                Berisi penjelasan mengenai <b>empat polutan utama</b> (CO, NO₂, SO₂, dan O₃), mencakup sumber, dampak, 
                serta penjelasan metode klasifikasi yang digunakan, yaitu SVM dengan kernel <i>Linear</i> dan <i>RBF</i>.
            </div>
        </div>

        <div class="panduan-container">
            <div class="panduan-title">5. Panduan</div>
            <div class="panduan-desc">
                Halaman yang sedang Anda baca. Menjelaskan secara ringkas fungsi setiap modul agar aplikasi dapat digunakan dengan lebih optimal.
            </div>
        </div>

        <div class="panduan-container">
            <div class="panduan-title">6. Tentang Pengembang</div>
            <div class="panduan-desc">
                Memuat profil pembuat aplikasi serta latar belakang singkat pengembangan sistem sebagai bagian dari penelitian.
            </div>
        </div>

        <div class="panduan-desc">
            Dengan memahami fungsi setiap modul di atas, pengguna dapat memanfaatkan aplikasi ini untuk eksplorasi data kualitas udara, 
            pelatihan model, dan interpretasi hasil secara interaktif dan menyeluruh.
        </div>
    """, unsafe_allow_html=True)