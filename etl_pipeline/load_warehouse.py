import os
import sqlite3
import pandas as pd

DB_PATH = "warehouse/steam_games_warehouse.db"

# =====================================================
# 1) SETUP & RESET DATA WAREHOUSE
# =====================================================

def reset_warehouse(db_path: str = DB_PATH):
    """
    Membuat ulang database dan menghapus tabel jika sudah ada.
    Aman dijalankan berulang kali.
    """

    os.makedirs("warehouse", exist_ok=True)

    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    cursor.execute("DROP TABLE IF EXISTS fact_game_metrics;")
    cursor.execute("DROP TABLE IF EXISTS dim_time;")
    cursor.execute("DROP TABLE IF EXISTS dim_game;")

    conn.commit()
    conn.close()

    print("✅ Warehouse siap (tabel di-reset)")


# =====================================================
# 2) LOAD DATA KE DATA WAREHOUSE
# =====================================================

def load_to_warehouse(df: pd.DataFrame, db_path: str = DB_PATH):
    """
    Load data hasil ETL ke data warehouse SQLite
    menggunakan skema star (dimensi + fakta).
    """

    conn = sqlite3.connect(db_path)

    # -----------------------------
    # DIMENSION: GAME
    # -----------------------------
    dim_game = df[
        ["appid", "name", "price", "genres", "developers", "is_free"]
    ].drop_duplicates(subset="appid")

    dim_game.to_sql(
        "dim_game",
        conn,
        if_exists="replace",
        index=False
    )

    # -----------------------------
    # DIMENSION: TIME
    # -----------------------------
    dim_time = df[
        ["appid", "release_year", "game_age_years"]
    ].drop_duplicates(subset="appid")

    dim_time.to_sql(
        "dim_time",
        conn,
        if_exists="replace",
        index=False
    )

    # -----------------------------
    # FACT TABLE
    # -----------------------------
    fact_game_metrics = df[
        [
            "appid",
            "total_reviews",
            "positive_ratio",
            "recommendations",
            "average_playtime_forever",
            "playtime_per_year",
            "metacritic_score",
            "user_score",
            "is_popular"
        ]
    ]

    fact_game_metrics.to_sql(
        "fact_game_metrics",
        conn,
        if_exists="replace",
        index=False
    )

    conn.close()

    print("✅ Load ke data warehouse selesai")
    print(f"Rows dim_game           : {len(dim_game):,}")
    print(f"Rows dim_time           : {len(dim_time):,}")
    print(f"Rows fact_game_metrics  : {len(fact_game_metrics):,}")
