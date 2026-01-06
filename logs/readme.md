# Pipeline Logs

Folder **logs/** digunakan untuk mendokumentasikan proses eksekusi
pipeline **ETL** dan **ELT** pada proyek Big Data ini.

Pada implementasi proyek ini, mekanisme logging **tidak disimpan dalam
file log terpisah**, melainkan **ditampilkan langsung pada output eksekusi**
(console / Google Colab notebook) menggunakan perintah `print()` pada
setiap tahap pipeline.

---

## 🧾 Mekanisme Logging

Informasi log akan muncul secara otomatis ketika pipeline dijalankan,
khususnya pada tahap berikut:

- Extract data dari Kaggle (CSV)
- Extract data dari Hugging Face (Dataset API)
- Load data ke data warehouse (SQLite)

Informasi yang ditampilkan meliputi:
- Sumber data
- Jumlah baris dan kolom
- Ukuran data
- Waktu eksekusi
- Status proses

Output ini berfungsi sebagai **bukti eksekusi pipeline**
dan digunakan untuk memverifikasi bahwa setiap tahap
ETL dan ELT telah berjalan dengan benar.

---

## 📌 Catatan Implementasi

Pendekatan logging berbasis output langsung dipilih untuk:
- Menjaga kesederhanaan implementasi
- Memudahkan observasi proses saat pengembangan
- Menyesuaikan dengan lingkungan berbasis notebook (Google Colab)

Meskipun tidak menggunakan file log terstruktur (CSV/JSON),
informasi log tetap dapat ditelusuri melalui riwayat output
saat pipeline dijalankan.

---

## 🔗 Referensi Eksekusi Pipeline

Contoh hasil logging dapat dilihat pada notebook berikut:
https://colab.research.google.com/drive/1kA9QZcD3PRhxx0_oGN05rAf3hDYxrQ_-?usp=sharing
