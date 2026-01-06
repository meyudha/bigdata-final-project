import pandas as pd

def validate_data(df: pd.DataFrame) -> dict:
    """
    Validasi kualitas data
    """

    return {
        "unique_appid": df["appid"].is_unique,
        "no_null_critical": df[["appid", "price"]].isnull().sum().sum() == 0,
        "price_non_negative": (df["price"] >= 0).all(),
        "positive_ratio_range": df["positive_ratio"].between(0, 1).all(),
        "game_age_non_negative": (df["game_age_years"] >= 0).all(),
        "price_variation": df["price"].nunique() > 1
    }

