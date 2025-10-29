Proyek Akhir: Bike Sharing Dataset - Iqlima Rahmawati

Deskripsi Proyek
Proyek ini menganalisis data peminjaman sepeda dan menampilkan dashboard interaktif menggunakan Streamlit
Notebook `.ipynb` berisi seluruh proses analisis data, mulai dari Gathering Data,Data Wrangling, Visualisasi, hingga Insight/Conclusion.

Struktur Folder
iqlima_bike_sharing_dataset
│
├─ dashboard/              # Folder kode dashboard
│   └─ dashboard.py
│
├─ data/                   # Folder dataset
│   ├─ day.csv
│   └─ hour.csv
├─ notebook.ipynb          # Notebook analisis data
├─ README.md               # File panduan ini
├─ requirements.txt        # Library yang digunakan
└─ url.txt                 # Link dashboard (Streamlit)

Persiapan Environment
1. Pastikan Python 3.13 sudah terinstall.
2. Masuk ke folder project: iqlima_bike_sharing_dataset

3. Install semua library yang dibutuhkan: 
pip install -r requirements.txt

Menjalankan Dashboard:
streamlit run dashboard/dashboard.py

Notebook Analysis
notebook.ipynb berisi seluruh proses analisis data:
Gathering Data
Data Wrangling
Visualisasi
Insight/Conclusion

Dashboard
Jika dashboard sudah di-deploy di Streamlit Cloud, masukkan link di file url.txt.
Contoh isi url.txt
https://iqlimarahmawati-bike-sharing-dataset--dashboarddashboard-qzliem.streamlit.app/
Catatan
Pastikan semua file .csv berada di folder data/.
Gunakan penamaan tahun, musim, atau kategori sesuai data asli agar dashboard menampilkan informasi yang jelas.
Jika ada error terkait library, pastikan semua package di requirements.txt sudah terinstall.

