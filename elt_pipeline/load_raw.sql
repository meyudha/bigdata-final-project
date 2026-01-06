-- ============================================
-- LOAD RAW DATA (ELT)
-- Data mentah langsung masuk warehouse
-- ============================================

DROP TABLE IF EXISTS raw_kaggle_steam_games;
DROP TABLE IF EXISTS raw_huggingface_steam_games;

CREATE TABLE raw_kaggle_steam_games AS
SELECT *
FROM read_csv_auto('raw/etl/kaggle/games.csv');

CREATE TABLE raw_huggingface_steam_games AS
SELECT *
FROM read_parquet('raw/api/huggingface/steam_games_raw.parquet');

