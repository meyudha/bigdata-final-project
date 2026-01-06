import pandas as pd
import numpy as np

def clean_data(df: pd.DataFrame) -> pd.DataFrame:
    """
    Data cleaning:
    - drop kolom index sisa CSV
    - validasi & dedup primary key (AppID)
    - handle missing value
    - standardisasi datetime
    - perbaikan kualitas kolom Name
    - outlier handling (IQR)
    """

    # Drop kolom index sisa CSV
    df = df.drop(columns=["Unnamed: 0", "unnamed_0"], errors="ignore")

    # Primary key
    df["AppID"] = pd.to_numeric(df["AppID"], errors="coerce")
    df = df.replace([np.inf, -np.inf], np.nan)
    df = df.dropna(subset=["AppID"])
    df["AppID"] = df["AppID"].astype("int64")
    df = df.drop_duplicates(subset="AppID")

    # Missing value handling
    num_cols = [
        "Price", "Required age", "DLC count", "DiscountDLC count",
        "Metacritic score", "Recommendations",
        "Average playtime forever", "Peak CCU",
        "Positive", "Negative"
    ]
    for col in num_cols:
        if col in df.columns:
            df[col] = df[col].fillna(0)

    cat_cols = ["Developers", "Publishers", "Categories", "Genres"]
    for col in cat_cols:
        if col in df.columns:
            df[col] = df[col].fillna("Unknown")

    text_cols = [
        "About the game", "Supported languages", "Full audio languages",
        "Reviews", "Website", "Support url", "Support email",
        "Notes", "Tags", "Screenshots", "Movies"
    ]
    for col in text_cols:
        if col in df.columns:
            df[col] = df[col].fillna("")

    # Datetime
    if "Release date" in df.columns:
        df["Release date"] = pd.to_datetime(df["Release date"], errors="coerce")

    # Outlier handling (Price – IQR)
    if "Price" in df.columns:
        Q1 = df["Price"].quantile(0.25)
        Q3 = df["Price"].quantile(0.75)
        IQR = Q3 - Q1
        df = df[
            (df["Price"] >= Q1 - 1.5 * IQR) &
            (df["Price"] <= Q3 + 1.5 * IQR)
        ]

    return df

