import numpy as np
import pandas as pd

def augment_data(df: pd.DataFrame, target_rows=100_000) -> pd.DataFrame:
    """
    Data augmentation untuk memenuhi minimal 100.000 baris
    """

    if df.shape[0] >= target_rows:
        return df

    needed = target_rows - df.shape[0]
    dummy = df.sample(n=needed, replace=True, random_state=42).copy()

    max_appid = df["appid"].max()
    dummy["appid"] = range(max_appid + 1, max_appid + 1 + needed)

    return pd.concat([df, dummy], ignore_index=True)
