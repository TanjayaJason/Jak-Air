import streamlit as st
import pandas as pd
import numpy as np
from io import BytesIO
from src_model import pipeline_training

def show():
    # === Styling ===
    st.markdown("""
        <style>
        .block-container { padding-top: 1rem !important; }
        h1, h2, h3, h4 { text-align: center !important; }
        h1 a, h2 a, h3 a, h4 a { display: none !important; }
        .stButton > button {
            background-color: #2E86C1;
            color: white;
            font-weight: 600;
            border-radius: 10px;
            transition: all 0.2s ease-in-out;
        }
        .stButton > button:hover {
            background-color: #1B4F72;
            transform: scale(1.03);
        }
        </style>
    """, unsafe_allow_html=True)

    st.markdown("<h1>Pelatihan & Pengujian Model</h1><hr>", unsafe_allow_html=True)

    # === Upload Dataset ===
    st.markdown("### 🧾 Upload Dataset")
    st.markdown("Silakan download template berikut, isi nilai polutan, dan kosongkan kolom kategori.")

    def download_template():
        template_df = pd.DataFrame({
            "so2_satelit": [], "co_satelit": [], "o3_satelit": [], "no2_satelit": [], "kategori_multivariat": []
        })
        output = BytesIO()
        with pd.ExcelWriter(output, engine="xlsxwriter") as writer:
            template_df.to_excel(writer, index=False, sheet_name="Template")
        st.download_button(
            label="📥 Download Template Dataset",
            data=output.getvalue(),
            file_name="template_dataset.xlsx",
            mime="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
        )
    download_template()

    uploaded_file = st.file_uploader("📤 Upload dataset Anda di sini:", type=["csv", "xlsx"])
    if uploaded_file is None:
        st.info("Silakan upload dataset terlebih dahulu untuk memulai pelatihan.")
        return

    df = pd.read_excel(uploaded_file) if uploaded_file.name.endswith(".xlsx") else pd.read_csv(uploaded_file)

    # === Validasi Dataset ===
    required_cols = {"so2_satelit", "co_satelit", "o3_satelit", "no2_satelit"}

    # 1. Cek kolom wajib
    if not required_cols.issubset(df.columns):
        st.error(f"Dataset tidak valid! Kolom wajib: {required_cols}")
        return

    # 2. Cek missing values
    if df[list(required_cols)].isnull().any().any():
        st.error("Dataset mengandung missing value. Harap bersihkan terlebih dahulu sebelum training.")
        return
    
    if "kategori_multivariat" in df.columns:
        if df["kategori_multivariat"].notnull().any() and df["kategori_multivariat"].astype(str).str.strip().ne("").any():
            st.error("Kolom 'kategori_multivariat' harus dikosongkan sebelum training.")
            return

    # 3. Cek tipe data numerik
    if not all(np.issubdtype(df[col].dtype, np.number) for col in list(required_cols)):
        st.error("Dataset harus berisi nilai numerik untuk semua parameter polutan.")
        return

    # 4. Cek dataset kosong
    if df.empty or len(df) < 10:
        st.error("Dataset terlalu sedikit. Minimal 10 baris data untuk melakukan training.")
        return

    st.dataframe(df.head(10), width="stretch")

    # === Hyperparameter Inputs ===
    st.markdown("### ⚙️ Hyperparameter SVM")
    col1, col2 = st.columns(2)
    with col1:
        C_val = st.number_input("Nilai Regularisasi (C)", min_value=0.01, max_value=1000.0, value=1.0, step=0.1)
    with col2:
        gamma_val = st.number_input("Nilai Gamma (RBF Kernel)", min_value=0.0001, max_value=10.0, value=0.1, step=0.01)

    # === Jalankan Training ===
    if st.button("🚀 Jalankan Pelatihan Model"):
        with st.spinner("Sedang melakukan cleansing, labeling, dan training model..."):
            cleaned_df, results, trained_models = pipeline_training.run_training(df, C_val, gamma_val)

        # Simpan hasil training di session_state
        st.session_state.cleaned_df = cleaned_df
        st.session_state.training_results = results
        st.session_state.trained_models = trained_models
        st.session_state.show_model_selection = True

        # Inisialisasi default model Linear
        st.session_state.kernel_choice = "Linear"
        st.session_state.selected_model = trained_models.get("linear_final")
        st.session_state.scaler = trained_models.get("scaler")
        st.session_state.feature_cols = trained_models.get("feature_cols")
        st.session_state.selected_params = {"kernel": "linear", "C": C_val, "gamma": gamma_val}

        st.success("✅ Pelatihan selesai! Silakan pilih model di bawah.")

    # === Bagian Pemilihan Model ===
    if st.session_state.get("show_model_selection", False):
        results = st.session_state.get("training_results")
        trained = st.session_state.get("trained_models")

        if results and trained:
            st.markdown("<hr><h2>✅ Pemilihan Model</h2>", unsafe_allow_html=True)

            # Pastikan ada key default kernel_choice
            if "kernel_choice" not in st.session_state:
                st.session_state.kernel_choice = "Linear"
                st.session_state.selected_model = trained_models.get("linear_final")
                st.session_state.scaler = trained.get("scaler")
                st.session_state.feature_cols = trained.get("feature_cols")
                st.session_state.selected_params = {"kernel": "linear", "C": C_val, "gamma": gamma_val}

            # Radio button kernel
            kernel_choice = st.radio(
                "Pilih Kernel SVM:",
                ("Linear", "RBF"),
                horizontal=True,
                key="kernel_choice"
            )

            if st.session_state.kernel_choice == "Linear":
                st.session_state.selected_model = trained.get("linear_final")
            else:
                st.session_state.selected_model = trained.get("rbf_final")
            st.session_state.selected_params = {
                "kernel": kernel_choice.lower(),
                "C": C_val,
                "gamma": gamma_val
            }

            # Tampilkan info model dan metrik
            col1, col2 = st.columns([1.2, 2])
            with col1:
                st.markdown(f"""
                    <div style="background-color:#f8f9fa; padding:12px; border-radius:10px; text-align:center; border:1px solid #dcdcdc;">
                        <b>Model terpilih:</b> {st.session_state.kernel_choice} Kernel<br>
                        <b>C:</b> {C_val} &nbsp; | &nbsp; <b>Gamma:</b> {gamma_val}
                    </div>
                """, unsafe_allow_html=True)

            with col2:
                metrics = results[st.session_state.kernel_choice]
                st.markdown("#### 📈 Hasil Evaluasi Model")
                for k, v in metrics.items():
                    if k != "Confusion Matrix":
                        st.write(f"**{k}:** {v:.4f}")

            # Form uji
            st.markdown("<hr><h2>Pengujian Model</h2>", unsafe_allow_html=True)
            show_testing_form()
        else:
            st.warning("Hasil pelatihan belum tersedia. Jalankan pelatihan terlebih dahulu.")

def compute_T2(x_row, mean_vec, cov_inv):
    x = np.array(x_row, dtype=float)
    return float((x - mean_vec) @ cov_inv @ (x - mean_vec).T)

def show_testing_form():
    with st.form("uji_form"):
        st.markdown("<p>Masukkan nilai polutan (mol/m²):</p>", unsafe_allow_html=True)
        col1, col2 = st.columns(2)
        col3, col4 = st.columns(2)
        so2 = col1.number_input("SO₂", value=0.0, step=0.0001, format="%.4f")
        co = col2.number_input("CO", value=0.0, step=0.0001, format="%.4f")
        o3 = col3.number_input("O₃", value=0.0, step=0.0001, format="%.4f")
        no2 = col4.number_input("NO₂", value=0.0, step=0.0001, format="%.4f")
        submit = st.form_submit_button("🔍 Prediksi")

    if submit:
        t2_param = st.session_state["trained_t2"]

        mean_vec = t2_param["mean"]
        cov_inv = t2_param["cov_inv"]
        t2_threshold = t2_param["UCL"]

        # Input user harus diurutkan sesuai feature_cols
        input_row = [so2, co, o3, no2]
        t2_user = compute_T2(input_row, mean_vec, cov_inv)

        st.session_state["t2_user"] = t2_user
        st.session_state["t2_threshold"] = t2_threshold

        model = st.session_state.selected_model
        scaler = st.session_state.scaler

        X = pd.DataFrame([[so2, co, o3, no2]], columns=st.session_state.feature_cols)
        X_scaled = scaler.transform(X)
        pred = model.predict(X_scaled)[0].strip().lower()

        st.session_state["hasil_keseluruhan"] = pred
        st.session_state.page = "📊 Hasil"
        st.session_state["polutan_input"] = {"so2": so2, "co": co, "o3": o3, "no2": no2}
        st.rerun()