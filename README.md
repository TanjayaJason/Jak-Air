# 🍃 Jak Air - Klasifikasi Kualitas Udara DKI Jakarta

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?style=for-the-badge&logo=python)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=for-the-badge&logo=Streamlit)
![Status](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)

**Jak Air** adalah aplikasi berbasis web untuk memantau dan mengklasifikasikan kualitas udara di wilayah **DKI Jakarta** menggunakan data satelit **Sentinel-5P**. Aplikasi ini memanfaatkan *Machine Learning* dengan algoritma **Support Vector Machine (SVM)** untuk menentukan kategori kualitas udara secara spasial dan temporal.

---

### 🚀 Demo Aplikasi
Coba aplikasi secara langsung tanpa instalasi melalui Hugging Face Spaces:

👉 **[Klik Disini untuk Membuka Jak Air](https://huggingface.co/spaces/TanjayaJason/Jak-Air)**

---

### 🌟 Fitur Utama

* **📊 Klasifikasi Multi-Kernel:** Mendukung pelatihan model SVM menggunakan kernel **Linear** dan **RBF (Radial Basis Function)**.
* **📡 Integrasi Sentinel-5P:** Menganalisis 4 polutan utama: **CO, NO₂, SO₂, dan O₃**.
* **🛠️ Pelatihan Mandiri:** Pengguna dapat mengunggah dataset sendiri, melakukan *cleansing*, *labeling* otomatis (menggunakan **Hotelling's T²**), dan melatih model.
* **🗺️ Visualisasi Interaktif:** Menampilkan hasil prediksi dalam bentuk peta sebaran wilayah DKI Jakarta dan grafik batang.
* **ℹ️ Edukasi:** Informasi lengkap mengenai dampak polutan dan metode klasifikasi.

---

### 🛠️ Teknologi yang Digunakan

* **Bahasa:** Python
* **Framework Web:** Streamlit
* **Machine Learning:** Scikit-Learn (SVM), Scipy
* **Data Processing:** Pandas, NumPy
* **Visualisasi & Geo:** Matplotlib, Seaborn, Geopandas

---

### 💻 Cara Menjalankan di Lokal

Jika Anda ingin menjalankan aplikasi ini di komputer Anda sendiri:

1.  **Clone Repositori**
    ```bash
    git clone [https://github.com/TanjayaJason/Jak-Air.git](https://github.com/TanjayaJason/Jak-Air.git)
    cd Jak-Air
    ```

2.  **Buat Virtual Environment (Opsional tapi Disarankan)**
    ```bash
    python -m venv venv
    # Windows:
    venv\Scripts\activate
    # Mac/Linux:
    source venv/bin/activate
    ```

3.  **Install Dependencies**
    ```bash
    pip install -r requirement.txt
    ```

4.  **Jalankan Aplikasi**
    ```bash
    streamlit run app.py
    ```

---

### 📂 Struktur Folder

```text
Jak-Air/
├── app.py                   # File utama aplikasi
├── requirement.txt          # Daftar pustaka Python
├── Data/                    # Data shapefile & gambar
├── halaman/                 # Modul halaman (Home, Hasil, Informasi, dll)
└── src_model/               # Pipeline pelatihan model (SVM & Preprocessing)