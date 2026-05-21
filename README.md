# 🏆 Sistem Seleksi Olimpiade Matematika
> Aplikasi berbasis Machine Learning untuk membantu guru/sekolah mengidentifikasi kesiapan siswa mengikuti olimpiade matematika.

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io)
![Python](https://img.shields.io/badge/Python-3.10+-blue)
![scikit-learn](https://img.shields.io/badge/scikit--learn-1.4.2-orange)
![License](https://img.shields.io/badge/License-MIT-green)

---

## 📌 Tentang Proyek

Sistem ini dikembangkan sebagai tugas Data Mining untuk **Prodi Pendidikan Matematika**. Menggunakan algoritma **Random Forest Classifier** untuk mengklasifikasikan kesiapan siswa berdasarkan 6 dimensi kemampuan matematika:

| Fitur | Deskripsi | Rentang |
|-------|-----------|---------|
| `NUM_ALJ` | Skor Numerasi Aljabar | 0–100 |
| `NUM_GEO` | Skor Numerasi Geometri | 0–100 |
| `NUM_BIL` | Skor Numerasi Bilangan | 0–100 |
| `NUM_DAT` | Skor Data & Ketidakpastian | 0–100 |
| `NUM_L3` | Skor Menalar | 0–100 |
| `LIT` | Skor Literasi | 0–100 |

## 🎯 Output Sistem

| Status | Kriteria | Keterangan |
|--------|----------|------------|
| 🏆 **Siap Olimpiade** | Rata-rata ≥ 80 & Min ≥ 65 | Layak ikut seleksi olimpiade |
| ⚡ **Potensial** | Rata-rata ≥ 60 & Min ≥ 45 | Perlu pembinaan lanjutan |
| ❌ **Tidak Siap** | Di bawah standar minimum | Perlu program remedial |

## 🚀 Cara Menggunakan

### A. Jalankan di Lokal

```bash
# 1. Clone repository
git clone https://github.com/USERNAME/olimpiade-math.git
cd olimpiade-math

# 2. Install dependencies
pip install -r requirements.txt

# 3. Jalankan aplikasi
streamlit run app.py
```

### B. Training Ulang Model (Google Colab)

1. Buka file `training_colab.ipynb` di Google Colab
2. Upload `dataset.xlsx` saat diminta
3. Jalankan semua cell secara berurutan
4. Download `model.pkl` dan `scaler.pkl` yang dihasilkan
5. Upload kedua file tersebut ke repository ini

## 📁 Struktur File

```
olimpiade-math/
├── app.py                  # Aplikasi Streamlit utama
├── model.pkl               # Model Random Forest (terlatih)
├── scaler.pkl              # StandardScaler untuk normalisasi
├── requirements.txt        # Daftar dependensi Python
├── training_colab.ipynb    # Notebook training di Google Colab
├── contoh_data.xlsx        # Contoh format file input
└── README.md               # Dokumentasi ini
```

## 📊 Performa Model

| Metrik | Nilai |
|--------|-------|
| Akurasi | **99%** |
| Precision (macro avg) | 0.99 |
| Recall (macro avg) | 0.98 |
| F1-Score (macro avg) | 0.98 |
| Metode | Random Forest (100 trees) |
| Dataset | 29,762 siswa |

## 📋 Format File Excel untuk Upload Batch

File Excel yang diunggah harus memiliki kolom berikut:

```
Nama (opsional) | NUM_ALJ | NUM_GEO | NUM_BIL | NUM_DAT | NUM_L3 | LIT
```

Contoh:
| Nama | NUM_ALJ | NUM_GEO | NUM_BIL | NUM_DAT | NUM_L3 | LIT |
|------|---------|---------|---------|---------|--------|-----|
| Budi | 85.5 | 80.0 | 90.0 | 78.0 | 88.0 | 92.0 |
| Ani  | 55.0 | 60.0 | 58.0 | 52.0 | 63.0 | 48.0 |

## 🛠️ Tech Stack

- **Frontend**: Streamlit
- **Machine Learning**: scikit-learn (Random Forest)
- **Data Processing**: Pandas, NumPy
- **Deployment**: Streamlit Community Cloud

## 📖 Cara Deploy ke Streamlit Cloud

1. Fork/clone repository ini ke akun GitHub kamu
2. Buka [share.streamlit.io](https://share.streamlit.io)
3. Login dengan akun GitHub
4. Klik **"New app"**
5. Pilih repository, branch `main`, dan file `app.py`
6. Klik **"Deploy!"**

---

*Dikembangkan untuk tugas Data Mining — Pendidikan Matematika*
