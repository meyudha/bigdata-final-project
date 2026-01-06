# ELT Pipeline

Folder ini berisi implementasi **pipeline ELT (Extract, Load, Transform)** pada proyek Big Data Steam Games Analytics.

Pendekatan ELT digunakan untuk memproses data dengan cara **memuat data mentah terlebih dahulu ke dalam data warehouse**, kemudian melakukan proses pembersihan, integrasi, dan feature engineering **langsung di dalam warehouse menggunakan SQL**.

---

## 📁 Struktur Folder

```text
elt_pipeline/
├── load_raw.sql
├── transform_elt.sql
└── aggregation.sql

