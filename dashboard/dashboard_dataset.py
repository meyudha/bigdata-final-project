# =====================================================
# DASHBOARD DATASET (CSV) – LOOKER STUDIO
# =====================================================

import pandas as pd
import sqlite3
import os
from google.colab import files

print("=== GENERATE DASHBOARD DATASET ===")

os.makedirs("dashboard", exist_ok=True)

conn = sqlite3.connect("warehouse/steam_games_warehouse.db")

dashboard_df = pd.read_sql("""
SELECT
    g.appid                    AS appid,
    g.name                     AS game_name,
    g.price                    AS price,
    g.is_free                  AS is_free,
    g.genres                   AS genres,
    g.developers               AS developers,
    t.release_year             AS release_year,
    t.game_age_years           AS game_age_years,
    f.total_reviews            AS total_reviews,
    f.positive_ratio           AS positive_ratio,
    f.recommendations          AS recommendations,
    f.average_playtime_forever AS avg_playtime_forever,
    f.playtime_per_year        AS playtime_per_year,
    f.metacritic_score         AS metacritic_score,
    f.user_score               AS user_score,
    f.is_popular               AS is_popular
FROM fact_game_metrics f
JOIN dim_game g ON f.appid = g.appid
JOIN dim_time t ON f.appid = t.appid
""", conn)

conn.close()

file_path = "dashboard/dashboard_dataset.csv"
dashboard_df.to_csv(file_path, index=False)

print("✅ Dashboard CSV siap")
print("Shape:", dashboard_df.shape)

files.download(file_path)

