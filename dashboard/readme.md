# Dashboard Dataset

Folder **dashboard** berisi dataset hasil akhir yang digunakan
sebagai sumber data untuk visualisasi pada **Google Looker Studio**.

Dataset pada folder ini dihasilkan dari proses query terhadap
data warehouse (SQLite) dan disimpan dalam format **CSV**.

---

## 📊 Dashboard Dataset

File utama:
- **dashboard_dataset.csv**

Dataset ini merupakan hasil penggabungan tabel fakta dan tabel dimensi,
yang mencakup informasi performa dan popularitas game Steam, seperti:
- Harga dan status game (gratis / berbayar)
- Genre dan developer
- Tahun rilis dan umur game
- Jumlah review dan rasio review positif
- Waktu bermain dan indikator popularitas

---

## 🔗 Integrasi dengan Looker Studio

CSV pada folder ini digunakan sebagai input data pada Google Looker Studio
melalui mode upload file CSV, bukan koneksi langsung ke database.

Pendekatan ini dipilih untuk mempermudah proses visualisasi dan
menyesuaikan dengan keterbatasan lingkungan pengembangan.

