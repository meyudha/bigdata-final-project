# Data Warehouse

Folder ini berisi **data warehouse** yang digunakan pada proyek *Big Data ETL & ELT – Steam Games Analytics*.

Data warehouse dibangun menggunakan **SQLite** dan berfungsi sebagai
penyimpanan data terstruktur hasil pemrosesan dari **pipeline ETL dan ELT**.
Seluruh data di dalam warehouse telah melalui tahap pembersihan,
standarisasi, dan feature engineering sehingga siap digunakan untuk
analisis lanjutan.

---

## 🗄️ Struktur Data Warehouse

Data warehouse menerapkan skema terstruktur yang terdiri dari tabel fakta
dan tabel dimensi sebagai berikut:

- **dim_game**  
  Menyimpan informasi utama terkait game, seperti identitas game,
  pengembang, genre, dan atribut statis lainnya.

- **dim_time**  
  Menyimpan informasi waktu yang digunakan untuk analisis berbasis
  temporal, seperti tahun rilis dan umur game.

- **fact_game_metrics**  
  Menyimpan metrik utama performa dan popularitas game, seperti jumlah
  review, rasio review positif, waktu bermain, dan indikator popularitas.

---

## 🎯 Peran Data Warehouse

Data yang tersimpan pada warehouse digunakan sebagai:
- Sumber utama untuk **query analitik**
- Basis data untuk **dashboard visualisasi**
- Media evaluasi dan perbandingan hasil pipeline **ETL dan ELT**

Dengan adanya data warehouse ini, proses analisis data game Steam
dapat dilakukan secara lebih terstruktur, konsisten, dan efisien.

