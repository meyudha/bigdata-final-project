import pandas as pd
import os
from datetime import datetime

def extract_source1():
    """
    Extract data mentah dari CSV Kaggle.
    File CSV diambil dari Google Drive dan sudah disalin ke folder raw/kaggle.
    Tidak dilakukan preprocessing atau cleaning.
    """

    start_time = datetime.now()
    source_name = "Kaggle CSV (Google Drive)"

    file_path = "raw/kaggle/games.csv"

    # READ ONLY (NO TRANSFORM)
    df_raw = pd.read_csv(file_path)

    exec_time = (datetime.now() - start_time).total_seconds()
    file_size_mb = round(os.path.getsize(file_path) / (1024 * 1024), 2)

    log = {
        "source": source_name,
        "file_path": file_path,
        "rows": df_raw.shape[0],
        "columns": df_raw.shape[1],
        "file_size_mb": file_size_mb,
        "execution_time_sec": exec_time,
        "timestamp": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    os.makedirs("logs/etl", exist_ok=True)
    pd.DataFrame([log]).to_csv(
        "logs/etl/extract_log.csv",
        mode="a",
        header=not os.path.exists("logs/etl/extract_log.csv"),
        index=False
    )

    print("=== Extract Source 1 (Kaggle CSV) Selesai ===")
    print(f"Baris  : {df_raw.shape[0]:,}")
    print(f"Kolom  : {df_raw.shape[1]}")
    print(f"Ukuran : {file_size_mb} MB")
    print(f"Waktu  : {exec_time:.2f} detik")

    return df_raw
