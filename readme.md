# 📊 ANALISIS DATA E-COMMERCE
## 👤 Author
Nama: Zahra Diya Nafilza
Kelas: XI RPL 5
Absen: 35

---

## 📌 Deskripsi Project
Project ini merupakan tugas praktikum Analisis dan Visualisasi Data menggunakan Python.  
Tujuan project ini adalah untuk melakukan:
- Data cleaning
- Analisis penjualan
- Visualisasi data
- Analisis korelasi antar variabel

Dataset:
data_penjualan.csv

---

## 📁 Struktur Folder

ecommerce-analysis/
│── main.py
│── data_praktikum_analisis_data - data_praktikum_analisis_data.csv
│── output/
│     ├── grafik_penjualan.png
│     ├── kategori_penjualan.png
│     └── korelasi.png
│── README.md

---

## ⚙️ Library yang Digunakan
- pandas
- matplotlib
- seaborn

Install:
pip install pandas matplotlib seaborn

---

## 🚀 Cara Menjalankan
1. Buka terminal di folder project
cd "C:\kka 2\ecommerce-analysis"

2. Jalankan program
python main.py

atau jika error:
py main.py

---

## 🧹 Tahapan Analisis

### 1. Load Data
Data diambil dari file CSV menggunakan pandas.

### 2. Data Cleaning
- Hapus data kosong
- Ubah format tanggal (Order_Date)
- Ubah tipe data numerik
- Hapus data tidak valid (harga <= 0)

### 3. Analisis Data

📈 Tren Penjualan Bulanan
Menampilkan total penjualan tiap bulan.

📊 Penjualan per Kategori
Menampilkan kategori produk dengan penjualan tertinggi.

🔥 Korelasi Antar Variabel
Melihat hubungan antara:
- Total Sales
- Ad Budget
- Quantity

---

## 📊 Hasil Analisis

- Penjualan memiliki pola naik turun setiap bulan
- Kategori produk memiliki performa berbeda
- Ad budget berpengaruh terhadap penjualan

---

## 📷 Dokumentasi
- Grafik tren penjualan
![Grafik Penjualan](output/grafik_penjualan.png)
- Bar chart kategori
![Kategori](output/kategori.png)
- Heatmap korelasi
![Korelasi](output/korelasi.png)
- Output terminal
![Data awal](output/data_awal.png)
![Analisis](output/analisis1.png)
![Analisis](output/analisis2.png)


---

## 🚀 Kesimpulan
Project ini membantu memahami:
- Cara cleaning data
- Analisis data dengan Python
- Visualisasi data
- Pengambilan insight bisnis

---

# 📊 ANALISIS D

---

## 📌 Deskripsi File
File ini (`analisis.py`) digunakan untuk melakukan analisis data lanjutan dari dataset e-commerce, meliputi:

- Identifikasi produk underperformer
- RFM Analysis (segmentasi pelanggan)
- Analisis efisiensi kategori produk
- Uji hipotesis pengaruh iklan
- Regresi linear (Ad Budget vs Sales)
- Analisis korelasi antar variabel
- Visualisasi data menggunakan matplotlib & seaborn

---

## 📁 Struktur Project

ecommerce-analysis/
│── main.py  
│── analisis.py  
│── data_praktikum_analisis_data.csv  
│── data_praktikum_analisis_data.xlsx  
│── output/  
│     ├── underperformer.png  
│     ├── efisiensi_kategori.png  
│     ├── perbandingan_iklan.png  
│     ├── regresi.png  
│     └── heatmap.png  
│── README.md  

---

## ⚙️ Library yang Digunakan
- pandas
- matplotlib
- seaborn
- scikit-learn
- openpyxl
- datetime

Install semua library:
pip install pandas matplotlib seaborn scikit-learn openpyxl

---

## 🚀 Cara Menjalankan

1. Masuk ke folder project:
cd "C:\kka 2\ecommerce-analysis"

2. Jalankan file analisis:
python analisis.py

atau:
py analisis.py

---

## 📊 Penjelasan Analisis

### 1. Underperformer Analysis
Menganalisis hubungan harga produk dan jumlah penjualan.

### 2. RFM Analysis
Segmentasi pelanggan berdasarkan:
- Recency
- Frequency
- Monetary

### 3. Efisiensi Kategori
Mengukur seberapa efektif kategori produk berdasarkan:
Total Sales / Ad Budget

### 4. Uji Hipotesis Iklan
Membandingkan penjualan berdasarkan:
- Budget iklan tinggi
- Budget iklan rendah

### 5. Regresi Linear
Menganalisis pengaruh Ad Budget terhadap Total Sales.

### 6. Heatmap Korelasi
Menampilkan hubungan antar variabel numerik dalam dataset.

---

## 📷 Output Visualisasi

Hasil analisis akan tersimpan di folder `output/`:

- underperformer.png
![underperformer](output/underperformer.png)
- efisiensi_kategori.png
![Kategori](output/efisiensi_kategori.png)
- perbandingan_iklan.png
![perbandingan](output/perbandingan_iklan.png)
- regresi.png
![regresi](output/regresi.png)
- heatmap.png
![heatmap](output/heatmap.png)

---

## 👥 Project Kelompok

### Tujuan:
- Melatih kerja sama tim dalam analisis data
- Membagi tugas dalam proses data science
- Menghasilkan insight bisnis dari data e-commerce

### Pembagian Umum:
- Data Cleaning: (nama anggota)
- Analisis Data: (nama anggota)
- Visualisasi: (nama anggota)
- Dokumentasi: (nama anggota)

---

## 🚀 Kesimpulan
File ini membantu dalam memahami:
- Analisis data lanjutan
- Segmentasi pelanggan (RFM)
- Hubungan antar variabel bisnis
- Pengaruh iklan terhadap penjualan
- Visualisasi data untuk insight