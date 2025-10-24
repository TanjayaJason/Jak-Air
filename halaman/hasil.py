import streamlit as st
import matplotlib.pyplot as plt
import geopandas as gpd

def show():
    st.markdown("""
        <style>
        .block-container { padding-top: 1rem !important; }
        h1, h2, h3, h4 { text-align: center !important; }
        h1 a, h2 a, h3 a, h4 a { display: none !important; }
        .param-card {
            background-color: #f8f9fa;
            border: 1px solid #dcdcdc;
            border-radius: 12px;
            padding: 15px 20px;
            margin-top: 10px;
            box-shadow: 2px 2px 8px rgba(0,0,0,0.05);
        }
        .param-card p {
            font-size: 15px;
            margin: 0.3rem 0;
        }
        .param-label {
            font-weight: 600;
            color: #2C3E50;
        }
        .param-value {
            color: #1A5276;
            font-weight: 600;
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1>Hasil</h1><hr>", unsafe_allow_html=True)

    if "hasil_keseluruhan" not in st.session_state:
        st.warning("⚠️ Jalankan pengujian terlebih dahulu.")
        return

    hasil = st.session_state["hasil_keseluruhan"].strip().lower()
    params = st.session_state.get("selected_params", {})

    warna_map = {
        "sehat": ("#d4edda", "#1AB63F", "✅"),
        "tidak sehat": ("#f8d7da", "#721c24", "⚠️"),
        "default": ("#e2e3e5", "#383d41", "ℹ️")
    }
    warna_bg, warna_teks, ikon = warna_map.get(hasil, warna_map["default"])

    st.markdown(
        f"""
        <div style="background-color:{warna_bg};color:{warna_teks};
            padding:15px;border-radius:10px;text-align:center;font-weight:600;margin-bottom:20px;">
            {ikon} Kualitas Udara Keseluruhan: <b>{hasil.upper()}</b>
        </div>
        """, unsafe_allow_html=True
    )

    # === Layout Hyperparam + Tab Visualisasi ===
    col1, col2 = st.columns([1, 2])
    with col1:
        st.subheader("Hyperparameter Model")
        if params:
            kernel = params.get("kernel", "N/A").upper()
            C_val = params.get("C", "N/A")
            gamma_val = params.get("gamma", "-")

            st.markdown(f"""
                <div class="param-card">
                    <p><span class="param-label">Kernel:</span> 
                        <span class="param-value">{kernel}</span></p>
                    <p><span class="param-label">C (Regularisasi):</span> 
                        <span class="param-value">{C_val}</span></p>
                    <p><span class="param-label">Gamma:</span> 
                        <span class="param-value">{gamma_val}</span></p>
                </div>
            """, unsafe_allow_html=True)
        else:
            st.info("Belum ada parameter model yang tersimpan.")

    with col2:
        # === Tabs untuk Peta dan Grafik Polutan ===
        tab1, tab2 = st.tabs(["🗺️ Peta Kualitas Udara", "📊 Grafik Polutan"])

        with tab1:
            try:
                jakarta = gpd.read_file("Data/Jakarta_Batas_Admin/dki_jakarta.shp")
                warna = {"sehat": "#7AE582", "tidak sehat": "#FF6B6B"}.get(hasil, "#B0B0B0")
                fig, ax = plt.subplots(figsize=(3.5, 3.5))
                jakarta.plot(ax=ax, color=warna, edgecolor="black", linewidth=1)
                ax.set_title(f"Peta Kualitas Udara DKI Jakarta — {hasil.upper()}",
                             fontsize=12, fontweight="bold")
                ax.axis("off")
                st.pyplot(fig)
            except Exception as e:
                st.error(f"Gagal menampilkan peta: {e}")

        with tab2:
            st.markdown("#### Nilai Polutan yang Diuji (µmol/m³)")
            polutan_data = st.session_state.get("polutan_input")

            if polutan_data:
                labels = ["SO₂", "CO", "O₃", "NO₂"]
                values = [
                    polutan_data.get("so2", 0),
                    polutan_data.get("co", 0),
                    polutan_data.get("o3", 0),
                    polutan_data.get("no2", 0)
                ]

                fig, ax = plt.subplots(figsize=(4, 3))
                bars = ax.bar(labels, values, color=["#5DADE2", "#48C9B0", "#F4D03F", "#E74C3C"])
                ax.set_ylabel("Konsentrasi (µmol/m³)")
                ax.set_title("Grafik Polutan Udara yang Diuji", fontsize=11, fontweight="bold", pad=10)

                # Tampilkan nilai di atas batang
                for bar in bars:
                    yval = bar.get_height()
                    ax.text(bar.get_x() + bar.get_width()/2, yval + 0.0005, f"{yval:.4f}",
                            ha='center', va='bottom', fontsize=9)
                st.pyplot(fig)
            else:
                st.info("Data polutan belum tersimpan dari pengujian.")

    st.markdown("<hr>", unsafe_allow_html=True)
    if st.button("🔙 Kembali ke Pengujian"):
        # Hapus session_state yang terkait hasil & pengujian
        for key in ["hasil_keseluruhan", "polutan_input", "selected_params", 
                    "selected_model", "kernel_choice", "show_model_selection",
                    "scaler", "feature_cols"]:
            if key in st.session_state:
                del st.session_state[key]

        # Kembali ke halaman pelatihan & pengujian
        st.session_state.page = "📊 Pelatihan & Pengujian"
        st.rerun()