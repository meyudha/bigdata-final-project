import numpy as np
import pandas as pd
from datetime import datetime

def feature_engineering(df: pd.DataFrame) -> pd.DataFrame:
    """
    Feature engineering (>=5 fitur):
    total_reviews, positive_ratio, is_free,
    release_year, game_age_years,
    playtime_per_year, is_popular
    """

    df["total_reviews"] = df["positive"] + df["negative"]
    df["positive_ratio"] = np.where(
        df["total_reviews"] > 0,
        df["positive"] / df["total_reviews"],
        0
    )

    df["is_free"] = (df["price"] == 0).astype(int)

    df["release_date"] = pd.to_datetime(df["release_date"], errors="coerce")
    df["release_year"] = df["release_date"].dt.year

    current_year = datetime.now().year
    df["game_age_years"] = (
        current_year - df["release_year"]
    ).fillna(0).clip(lower=0).astype(int)

    df["playtime_per_year"] = np.where(
        df["game_age_years"] > 0,
        df["average_playtime_forever"] / df["game_age_years"],
        df["average_playtime_forever"]
    )

    pop_threshold = df["total_reviews"].quantile(0.90)
    df["is_popular"] = (df["total_reviews"] >= pop_threshold).astype(int)

    return df

