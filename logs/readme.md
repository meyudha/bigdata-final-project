# Pipeline Logs

Folder **logs** digunakan untuk mendokumentasikan proses eksekusi
pipeline ETL dan ELT pada proyek ini.

Pada implementasi ini, proses logging **tidak disimpan dalam file terpisah**,
melainkan **ditampilkan langsung pada output eksekusi (console / notebook)**
melalui perintah `print()` pada masing-masing tahap pipeline.

---

## 🧾 Mekanisme Logging

Informasi log dicetak secara langsung saat pipeline dijalankan,
terutama pada tahap:
- Extract data dari Kaggle
- Extract data dari Hugging Face
- Load data ke warehouse

Informasi yang ditampilkan meliputi:
- Sumber data
- Jumlah baris dan kolom
- Ukuran data
- Waktu eksekusi

Output log ini digunakan sebagai bukti bahwa setiap tahap pipeline
berhasil dijalankan dan dapat diamati secara langsung.

---

## 📌 Catatan

Pendekatan logging ini dipilih untuk menjaga kesederhanaan implementasi
serta menyesuaikan dengan lingkungan pengembangan berbasis notebook.
