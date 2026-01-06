import pandas as pd
import os
from datetime import datetime
from datasets import load_dataset

def extract_source2():
    """
    Extract data mentah dari Hugging Face Dataset API.
    Tidak ada preprocessing atau cleaning.
    """

    start_time = datetime.now()

    dataset = load_dataset(
        "FronkonGames/steam-games-dataset",
        split="train"
    )

    df_raw = pd.DataFrame(dataset)

    # Simpan raw data
    os.makedirs("raw/api/huggingface", exist_ok=True)
    raw_path = "raw/api/huggingface/steam_games_raw.parquet"
    df_raw.to_parquet(raw_path, index=False)

    exec_time = (datetime.now() - start_time).total_seconds()
    file_size_mb = round(os.path.getsize(raw_path) / (1024 * 1024), 2)

    log = {
        "source": "Hugging Face Dataset API",
        "dataset_name": "FronkonGames/steam-games-dataset",
        "split": "train",
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

    print("=== Extract Hugging Face Selesai ===")
    print("Dataset : FronkonGames/steam-games-dataset (train)")
    print(f"Baris   : {df_raw.shape[0]:,}")
    print(f"Kolom   : {df_raw.shape[1]}")
    print(f"Ukuran  : {file_size_mb} MB")
    print(f"Waktu   : {exec_time:.2f} detik")

    return df_raw

