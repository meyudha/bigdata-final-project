-- ============================================
-- ELT FEATURE ENGINEERING & ANALYTICS
-- ============================================

DROP TABLE IF EXISTS elt_analytics_games;

CREATE TABLE elt_analytics_games AS
SELECT
    appid,
    name,
    price,
    positive,
    negative,
    recommendations,
    average_playtime_forever,
    genres,
    developers,
    release_date,
    metacritic_score,
    user_score,

    -- Feature Engineering
    (positive + negative) AS total_reviews,

    CASE
        WHEN (positive + negative) > 0
        THEN ROUND(positive * 1.0 / (positive + negative), 4)
        ELSE 0
    END AS positive_ratio,

    CASE
        WHEN price = 0 THEN 1 ELSE 0
    END AS is_free,

    CAST(strftime('%Y', release_date) AS INTEGER) AS release_year,

    CASE
        WHEN release_date IS NOT NULL
        THEN CAST(strftime('%Y', 'now') AS INTEGER)
             - CAST(strftime('%Y', release_date) AS INTEGER)
        ELSE 0
    END AS game_age_years

FROM elt_clean_games;

