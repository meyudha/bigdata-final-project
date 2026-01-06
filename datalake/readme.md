# Data Lake

Folder **datalake** digunakan sebagai penyimpanan terpusat untuk **data mentah (raw data)**
yang dikumpulkan dari berbagai sumber pada proyek ini.

Data yang disimpan di dalam datalake masih berada dalam kondisi asli
tanpa melalui proses pembersihan, transformasi, maupun integrasi.
Hal ini bertujuan untuk menjaga keutuhan data sumber sebelum diproses
lebih lanjut pada pipeline ETL dan ELT.

---

## 📂 Sumber Data

Data mentah yang disimpan dalam datalake berasal dari:
1. **Kaggle** – dataset game Steam dalam format **CSV**
2. **Hugging Face (Dataset API)** – dataset game Steam dalam format **Parquet**

Setiap sumber data disimpan secara terpisah untuk memudahkan
pelacakan asal data (data lineage) dan pengelolaan data multisumber.

---

## 🔗 Peran Data Lake

Datalake berperan sebagai:
- Tempat penyimpanan awal data hasil proses **extract**
- Penghubung antara sumber data dengan pipeline **ETL dan ELT**
- Cadangan data mentah yang dapat digunakan kembali jika diperlukan

Dengan adanya datalake, proses pengolahan data menjadi lebih terstruktur
dan mendukung pengembangan pipeline Big Data yang fleksibel.
