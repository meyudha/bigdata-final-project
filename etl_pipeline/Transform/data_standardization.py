import pandas as pd

def standardize_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Standardisasi:
    - snake_case
    - normalisasi numerik
    - encoding kategorikal
    - konsistensi tipe data
    """

    df.columns = (
        df.columns.str.strip()
        .str.lower()
        .str.replace(r"[^\w]+", "_", regex=True)
    )

    # Normalisasi
    for src, tgt in {
        "price": "price_norm",
        "average_playtime_forever": "avg_playtime_norm"
    }.items():
        if src in df.columns:
            col_min, col_max = df[src].min(), df[src].max()
            df[tgt] = (
                (df[src] - col_min) / (col_max - col_min)
                if col_max > col_min else 0.0
            )

    # Encoding
    if "dlc_count" in df.columns:
        df["has_dlc"] = (df["dlc_count"] > 0).astype(int)

    return df
