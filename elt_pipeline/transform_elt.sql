-- ============================================
-- ELT TRANSFORM
-- Cleaning & integrasi via SQL
-- ============================================

DROP TABLE IF EXISTS elt_clean_games;

CREATE TABLE elt_clean_games AS
SELECT
    CAST(AppID AS INTEGER)               AS appid,
    COALESCE(NULLIF(Name, ''), 'Unknown') AS name,
    CAST(Price AS REAL)                  AS price,
    CAST(Positive AS INTEGER)            AS positive,
    CAST(Negative AS INTEGER)            AS negative,
    CAST(Recommendations AS INTEGER)     AS recommendations,
    CAST("Average playtime forever" AS REAL) AS average_playtime_forever,
    Genres,
    Developers,
    DATE("Release date")                 AS release_date,
    CAST("Metacritic score" AS INTEGER)  AS metacritic_score,
    CAST("User score" AS INTEGER)        AS user_score
FROM raw_kaggle_steam_games
WHERE AppID IS NOT NULL;

