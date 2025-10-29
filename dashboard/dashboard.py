# ===============================
# DASHBOARD BIKE SHARING - IQLIMA
# ===============================

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ===============================
# KONFIGURASI HALAMAN
# ===============================
st.set_page_config(page_title="Dashboard Bike Sharing", layout="wide")

# ===============================
# LOAD DATA
# ===============================
@st.cache_data
def load_data():
#LOAD CSV
    df_day = pd.read_csv("data/day.csv")
    df_hour = pd.read_csv("data/hour.csv")

# Mapping season (1-4) ke kategori
    season_map = {1: "Spring", 2: "Summer", 3: "Fall", 4: "Winter"}
    df_day['season'] = df_day['season'].map(season_map)
    df_hour['season'] = df_hour['season'].map(season_map)

# Mapping tahun 0/1 ke tahun asli
    df_day['year'] = df_day['yr'].map({0: 2011, 1: 2012})
    df_hour['year'] = df_hour['yr'].map({0: 2011, 1: 2012})
    return df_day, df_hour

df_day, df_hour = load_data()

# ===============================
# SIDEBAR FILTER
# ===============================
st.sidebar.header("Filter Dashboard")
selected_year = st.sidebar.selectbox("Pilih Tahun:", sorted(df_day['year'].unique()))
selected_seasons = st.sidebar.multiselect(
"Pilih Musim:",
df_day['season'].unique(),
default=list(df_day['season'].unique())
)

# Filter dataframe sesuai pilihan
df_day_filtered = df_day[
(df_day['year'] == selected_year) & (df_day['season'].isin(selected_seasons))
]
df_hour_filtered = df_hour[
(df_hour['year'] == selected_year) & (df_hour['season'].isin(selected_seasons))
]

# ===============================
# HEADER
# ===============================
st.title("Dashboard Analisis Data Bike Sharing")
st.markdown("Proyek Akhir - Dicoding by Iqlima Rahmawati")

# ===============================
# KPI
# ===============================
col1, col2, col3 = st.columns(3)
col1.metric("Total Peminjaman", f"{df_day_filtered['cnt'].sum():,}")
col2.metric("Rata-rata Peminjaman Harian", f"{df_day_filtered['cnt'].mean():.0f}")
col3.metric("Jumlah Hari Data", len(df_day_filtered))

st.markdown("---")

# ===============================
# VISUALISASI 1: Tren Peminjaman per Bulan
# ===============================
st.subheader("Tren Peminjaman Sepeda per Bulan")
monthly = df_day_filtered.groupby("mnth")["cnt"].sum().reset_index()
fig1, ax1 = plt.subplots(figsize=(10,5))
sns.lineplot(data=monthly, x="mnth", y="cnt", marker="o", ax=ax1, color="teal")
ax1.set_xlabel("Bulan")
ax1.set_ylabel("Jumlah Peminjaman")
ax1.set_title(f"Tren Jumlah Peminjaman Tahun {selected_year}")
st.pyplot(fig1)

# Insight
st.markdown("""
**Insight:**
Jumlah peminjaman meningkat signifikan pada bulan musim panas (Summer), menunjukkan pengaruh cuaca hangat terhadap aktivitas bersepeda.
""")

# ===============================
# VISUALISASI 2: Hari Kerja vs Hari Libur
# ===============================
st.subheader("Perbandingan Hari Kerja dan Hari Libur")
fig2, ax2 = plt.subplots(figsize=(8,5))
sns.barplot(
data=df_day_filtered,
x="workingday",
y="cnt",
palette="coolwarm",
ax=ax2
)
ax2.set_xlabel("Working Day (0 = Libur, 1 = Hari Kerja)")
ax2.set_ylabel("Jumlah Peminjaman")
ax2.set_title("Jumlah Peminjaman Hari Kerja vs Hari Libur")
st.pyplot(fig2)

# Insight
st.markdown("""
**Insight:**
Peminjaman pada hari kerja dan hari libur relatif seimbang, menunjukkan layanan digunakan baik untuk aktivitas rutin maupun rekreasi.
""")

st.success("✅ Dashboard berhasil ditampilkan!")
