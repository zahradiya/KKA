import os
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import datetime as dt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

sns.set(style="whitegrid")

# =====================================================
# BUAT FOLDER OUTPUT JIKA BELUM ADA
# =====================================================

if not os.path.exists("output"):
    os.makedirs("output")

# =====================================================
# LOAD DATA
# =====================================================

df = pd.read_csv("data_praktikum_analisis_data.csv")

print("DATA AWAL")
print(df.head())

# =====================================================
# DATA WRANGLING
# =====================================================

df["Order_Date"] = pd.to_datetime(df["Order_Date"], errors="coerce")
df = df.dropna()

print("\nINFO DATA")
print(df.info())

print("\nMISSING VALUE")
print(df.isnull().sum())

# =====================================================
# 1. IDENTIFIKASI PRODUK UNDERPERFORMER
# =====================================================

avg_price = df["Price_Per_Unit"].mean()

underperformer = df[df["Price_Per_Unit"] < avg_price]

print("\nPRODUK UNDERPERFORMER")
print(underperformer.groupby("Product_Category")["Quantity"].sum())

plt.figure(figsize=(12,7))

sns.scatterplot(
    data=df,
    x="Price_Per_Unit",
    y="Quantity",
    hue="Product_Category",
    palette="bright",
    s=120,
    alpha=0.8
)

plt.axvline(avg_price, color="red", linestyle="--", linewidth=2)

plt.title("Identifikasi Produk Underperformer")
plt.xlabel("Price Per Unit")
plt.ylabel("Quantity Sold")

plt.tight_layout()
plt.savefig("output/underperformer.png")
plt.show()

# =====================================================
# 2. RFM ANALYSIS
# =====================================================

snapshot_date = df["Order_Date"].max() + dt.timedelta(days=1)

rfm = df.groupby("CustomerID").agg({
    "Order_Date": lambda x: (snapshot_date - x.max()).days,
    "Order_ID": "count",
    "Total_Sales": "sum"
})

rfm.columns = ["Recency","Frequency","Monetary"]

print("\nRFM ANALYSIS")
print(rfm.head())

rfm["R_Score"] = pd.qcut(rfm["Recency"],5,labels=[5,4,3,2,1])
rfm["F_Score"] = pd.qcut(rfm["Frequency"].rank(method="first"),5,labels=[1,2,3,4,5])
rfm["M_Score"] = pd.qcut(rfm["Monetary"],5,labels=[1,2,3,4,5])

rfm["RFM_Group"] = (
    rfm["R_Score"].astype(str) +
    rfm["F_Score"].astype(str) +
    rfm["M_Score"].astype(str)
)

print("\nRFM GROUP")
print(rfm.head())

# =====================================================
# 3. EFISIENSI KATEGORI
# =====================================================

category_analysis = df.groupby("Product_Category").agg({
    "Total_Sales":"sum",
    "Ad_Budget":"sum"
})

category_analysis["Efficiency"] = (
    category_analysis["Total_Sales"] /
    category_analysis["Ad_Budget"]
)

category_analysis = category_analysis.sort_values("Efficiency")

print("\nEFISIENSI KATEGORI")
print(category_analysis)

plt.figure(figsize=(10,6))

sns.barplot(
    x=category_analysis["Efficiency"],
    y=category_analysis.index,
    palette="magma"
)

plt.title("Efisiensi Kategori Produk")
plt.xlabel("Efficiency")

plt.tight_layout()
plt.savefig("output/efisiensi_kategori.png")
plt.show()

median_ad = df["Ad_Budget"].median()

high_ads = df[df["Ad_Budget"] > median_ad]
low_ads = df[df["Ad_Budget"] <= median_ad]

comparison = pd.DataFrame({
    "Group":["High Ads","Low Ads"],
    "Average Sales":[
        high_ads["Total_Sales"].mean(),
        low_ads["Total_Sales"].mean()
    ]
})

plt.figure(figsize=(8,6))

sns.barplot(
    data=comparison,
    x="Group",
    y="Average Sales",
    palette="Set2"
)

plt.title("Perbandingan Penjualan Berdasarkan Iklan")

plt.tight_layout()
plt.savefig("output/perbandingan_iklan.png")
plt.show()


X = df[["Ad_Budget"]]
y = df["Total_Sales"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

model = LinearRegression()
model.fit(X_train, y_train)

print("\nREGRESI LINEAR")
print("Koefisien:", model.coef_[0])
print("R2 Score:", model.score(X_test, y_test))

plt.figure(figsize=(10,6))

sns.regplot(
    x="Ad_Budget",
    y="Total_Sales",
    data=df,
    scatter_kws={"alpha":0.6,"s":80},
    line_kws={"color":"red"}
)

plt.title("Hubungan Ad Budget dengan Sales")

plt.tight_layout()
plt.savefig("output/regresi.png")
plt.show()


plt.figure(figsize=(8,6))

corr = df[["Price_Per_Unit","Quantity","Ad_Budget","Total_Sales"]].corr()

sns.heatmap(corr, annot=True, cmap="coolwarm", fmt=".2f")

plt.title("Heatmap Korelasi")

plt.tight_layout()
plt.savefig("output/heatmap.png")
plt.show()

print("\nSEMUA ANALISIS SELESAI ✔")