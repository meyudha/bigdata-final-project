# Big Data ETL & ELT Pipeline – Steam Games Analytics

## 📌 Deskripsi Studi Kasus
Proyek ini merupakan implementasi **pipeline Big Data** menggunakan pendekatan **ETL (Extract, Transform, Load)** dan **ELT (Extract, Load, Transform)** pada studi kasus **data game Steam**.  
Data yang digunakan berasal dari beberapa sumber dan diolah untuk menganalisis **performa dan popularitas game**, kemudian disajikan dalam bentuk **dashboard analitik**.

---

## 🏗️ Arsitektur Sistem (Ringkas)
Alur sistem secara umum adalah sebagai berikut:
1. Data diambil dari beberapa sumber (CSV dan API)
2. Data mentah disimpan sebagai **raw data**
3. Data diproses melalui dua jalur:
   - **ETL**: data dibersihkan dan ditransformasi terlebih dahulu sebelum masuk ke warehouse
   - **ELT**: data mentah langsung dimasukkan ke warehouse, transformasi dilakukan di dalam warehouse
4. Data warehouse digunakan sebagai sumber data analitik
5. Hasil analisis ditampilkan dalam **dashboard Google Looker Studio**

---

## 🔄 Perbedaan ETL dan ELT pada Proyek Ini

| Aspek | ETL | ELT |
|-----|----|----|
| Urutan proses | Transform → Load | Load → Transform |
| Lokasi transformasi | Python (sebelum warehouse) | SQL (di dalam warehouse) |
| Fleksibilitas | Lebih kaku | Lebih fleksibel |
| Kegunaan | Data final untuk dashboard | Eksplorasi dan analisis ad-hoc |

---

## 🗂️ Struktur Direktori
Struktur repositori mengikuti ketentuan penilaian dan **tidak diubah secara substansial**:

bigdata-final-project/
├── etl_pipeline/ # Script pipeline ETL (Python)
├── elt_pipeline/ # Script pipeline ELT (SQL / Python)
├── raw/ # Data mentah dari masing-masing sumber
├── datalake/ # Penyimpanan raw data terpusat
├── warehouse/ # Data warehouse (SQLite)
├── dashboard/ # Dataset CSV untuk Looker Studio
├── logs/ # Log proses ETL & ELT
├── architecture/ # Diagram arsitektur sistem
└── README.md


---

## ▶️ Cara Menjalankan Pipeline

### 1️⃣ Menjalankan Pipeline ETL
Pipeline ETL digunakan untuk menghasilkan data bersih dan siap analisis.

```bash
python etl_pipeline/run_etl.py
