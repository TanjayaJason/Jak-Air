import numpy as np
import pandas as pd
from scipy.stats import f
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC
from sklearn.metrics import (
    accuracy_score,
    f1_score,
    precision_score,
    recall_score,
    confusion_matrix
)
import seaborn as sns
import matplotlib.pyplot as plt
import streamlit as st

def run_training(df, C_val, gamma_val):
    st.markdown("### 1️⃣ Cleansing Data")

    # Normalisasi kolom
    df = df.copy()
    df.columns = df.columns.astype(str).str.strip().str.lower()

    feature_cols = ["so2_satelit", "co_satelit", "o3_satelit", "no2_satelit"]
    missing_cols = [c for c in feature_cols if c not in df.columns]
    if missing_cols:
        st.error(f"Dataset tidak valid — kolom hilang: {missing_cols}")
        st.stop()

    # Hapus baris bernilai 0
    mask_nonzero = (df[feature_cols] != 0).all(axis=1)
    df_clean = df[mask_nonzero].reset_index(drop=True)
    st.markdown("Penghapusan baris dengan nilai 0 pada semua fitur")
    st.write(f"Jumlah data setelah cleansing: {len(df_clean)} dari {len(df)}")

    if df_clean.empty:
        st.error("Semua data terhapus saat cleansing. Pastikan tidak semua nilai = 0.")
        st.stop()

    # === 2️⃣ Labeling Hotelling’s T² ===
    st.markdown("### 2️⃣ Labeling (Hotelling's T²)")
    X = df_clean[feature_cols].astype(float).values
    n, p = X.shape

    cov_mat = np.cov(X, rowvar=False)
    try:
        cov_inv = np.linalg.inv(cov_mat)
    except np.linalg.LinAlgError:
        st.warning("Covariance singular — menambahkan regularisasi kecil.")
        cov_mat += np.eye(p) * 1e-6
        cov_inv = np.linalg.inv(cov_mat)

    mean_vec = np.mean(X, axis=0)
    T2_values = [float((x - mean_vec) @ cov_inv @ (x - mean_vec).T) for x in X]
    df_clean["T2_stat"] = T2_values

    alpha = 0.01
    UCL = (p * (n - 1) / (n - p)) * f.ppf(1 - alpha, p, n - p) if n > p else np.nan
    if np.isnan(UCL):
        st.error("UCL tidak dapat dihitung karena n <= p.")
        st.stop()
    st.write(f"**Upper Control Limit (UCL)** untuk T²: {UCL:.4f}")    

    # Label lowercase supaya konsisten
    df_clean["kategori_multivariat"] = np.where(
        df_clean["T2_stat"] > UCL, "tidak sehat", "sehat"
    )

    # Ringkasan kategori
    st.markdown("#### Ringkasan Kategori")
    label_counts = df_clean["kategori_multivariat"].value_counts()
    col1, col2 = st.columns(2)
    with col1:
        st.metric("Jumlah Sehat", label_counts.get("sehat", 0))
    with col2:
        st.metric("Jumlah Tidak Sehat", label_counts.get("tidak sehat", 0))

    st.write("Preview data setelah labeling:")
    st.dataframe(df_clean.head(10))

    # === 3️⃣ Training Model SVM ===
    st.markdown("### 3️⃣ Training Model Custom (SVM)")
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df_clean[feature_cols])
    y = df_clean["kategori_multivariat"]

    X_train, X_test, y_train, y_test = train_test_split(
        X_scaled,
        y,
        test_size=0.2,
        random_state=42,
        stratify=y
    )

    linear_model = SVC(kernel='linear', C=C_val)
    rbf_model = SVC(kernel='rbf', C=C_val, gamma=gamma_val)

    linear_model.fit(X_train, y_train)
    rbf_model.fit(X_train, y_train)

    y_pred_linear = linear_model.predict(X_test)
    y_pred_rbf = rbf_model.predict(X_test)

    results = {
        "Linear": {
            "Accuracy": accuracy_score(y_test, y_pred_linear),
            "Precision": precision_score(y_test, y_pred_linear, average="weighted", zero_division=0),
            "Recall": recall_score(y_test, y_pred_linear, average="weighted", zero_division=0),
            "F1 Score": f1_score(y_test, y_pred_linear, average="weighted"),
            "Confusion Matrix": confusion_matrix(y_test, y_pred_linear)
        },
        "RBF": {
            "Accuracy": accuracy_score(y_test, y_pred_rbf),
            "Precision": precision_score(y_test, y_pred_rbf, average="weighted", zero_division=0),
            "Recall": recall_score(y_test, y_pred_rbf, average="weighted", zero_division=0),
            "F1 Score": f1_score(y_test, y_pred_rbf, average="weighted"),
            "Confusion Matrix": confusion_matrix(y_test, y_pred_rbf)
        }
    }

    # === 4️⃣ Tampilkan hasil ===
    st.markdown("#### 🔍 Perbandingan Model")
    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Linear Kernel")
        for m, v in results["Linear"].items():
            if m != "Confusion Matrix":
                st.write(f"**{m}:** {v:.4f}")
        fig, ax = plt.subplots()
        sns.heatmap(results["Linear"]["Confusion Matrix"], annot=True, fmt="d", cmap="Blues", ax=ax)
        st.pyplot(fig)

    with col2:
        st.subheader("RBF Kernel")
        for m, v in results["RBF"].items():
            if m != "Confusion Matrix":
                st.write(f"**{m}:** {v:.4f}")
        fig, ax = plt.subplots()
        sns.heatmap(results["RBF"]["Confusion Matrix"], annot=True, fmt="d", cmap="Blues", ax=ax)
        st.pyplot(fig)

    # Simpan hasil training
    trained_models = {
        "linear": linear_model,
        "rbf": rbf_model,
        "scaler": scaler,
        "feature_cols": feature_cols,
    }
    st.session_state["trained_models"] = trained_models
    st.session_state["training_results"] = results

    return df_clean, results, trained_models