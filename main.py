import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# =========================
# BUAT FOLDER OUTPUT
# =========================
if not os.path.exists('output'):
    os.makedirs('output')

# =========================
# 1. LOAD DATA (PAKAI NAMA FILE KAMU)
# =========================
df = pd.read_csv('data_praktikum_analisis_data.csv')

print("\n=== DATA AWAL ===")
print(df.head())
print("\nJumlah data:", len(df))

# =========================
# 2. CLEANING DATA
# =========================
df = df.dropna()

df['Order_Date'] = pd.to_datetime(df['Order_Date'], errors='coerce')
df = df.dropna(subset=['Order_Date'])

# convert numeric
num_cols = ['Total_Sales', 'Ad_Budget', 'Quantity', 'Price_Per_Unit']
for col in num_cols:
    df[col] = pd.to_numeric(df[col], errors='coerce')

df = df.dropna()
df = df[df['Price_Per_Unit'] > 0]

print("\nJumlah data setelah cleaning:", len(df))

# =========================
# 3. TREND PENJUALAN
# =========================
df['Month'] = df['Order_Date'].dt.to_period('M').astype(str)

monthly_sales = df.groupby('Month')['Total_Sales'].sum()

plt.figure(figsize=(10,5))
plt.plot(monthly_sales.index, monthly_sales.values, marker='o')
plt.title('Tren Penjualan Bulanan')
plt.xticks(rotation=45)
plt.grid()

plt.savefig('output/grafik_penjualan.png')
plt.show()

# =========================
# 4. PENJUALAN PER KATEGORI
# =========================
category_sales = df.groupby('Product_Category')['Total_Sales'].sum()

plt.figure(figsize=(8,5))
category_sales.plot(kind='bar')
plt.title('Penjualan per Kategori')
plt.xticks(rotation=45)
plt.grid(axis='y')

plt.savefig('output/kategori_penjualan.png')
plt.show()

# =========================
# 5. KORELASI
# =========================
correlation = df[['Total_Sales', 'Ad_Budget', 'Quantity']].corr()

plt.figure(figsize=(6,4))
sns.heatmap(correlation, annot=True, cmap='coolwarm')
plt.title('Korelasi Antar Variabel')

plt.savefig('output/korelasi.png')
plt.show()

# =========================
# 6. OUTPUT TEKS
# =========================
print("\n=== HASIL ANALISIS ===")
print("\nMonthly Sales:")
print(monthly_sales)

print("\nCategory Sales:")
print(category_sales)

print("\nCorrelation:")
print(correlation)