# Pipeline Logs

Folder **logs** berisi catatan (log) eksekusi pipeline ETL dan ELT
yang dihasilkan secara otomatis oleh masing-masing script.

Log **tidak dibuat secara terpusat**, melainkan dicatat langsung
pada setiap tahap proses (extract, load, atau transform) di dalam
kode Python maupun SQL yang dijalankan.

---

## 🧾 Mekanisme Logging

Proses logging dilakukan sebagai berikut:
- Setiap script ETL dan ELT mencatat informasi prosesnya sendiri
- Log disimpan dalam format CSV
- Penulisan log dilakukan secara append (berurutan sesuai eksekusi)

Pendekatan ini dipilih agar setiap tahap pipeline memiliki
catatan eksekusi yang jelas dan terpisah.

---

## 📁 Struktur Log

- **logs/etl/**  
  Berisi log proses ETL, seperti:
  - extract data dari Kaggle
  - extract data dari Hugging Face

- **logs/elt/**  
  Berisi log proses ELT, seperti:
  - load data mentah ke warehouse
  - transformasi berbasis SQL (jika dicatat)

---

## 📌 Informasi yang Dicatat

Setiap log mencakup informasi penting, antara lain:
- Sumber data atau proses
- Jumlah baris dan kolom
- Ukuran data
- Waktu eksekusi
- Timestamp proses

Log ini digunakan sebagai bukti bahwa pipeline
dijalankan secara terstruktur dan terdokumentasi.

