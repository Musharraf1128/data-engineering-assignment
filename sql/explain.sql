-- Before index

EXPLAIN ANALYZE
SELECT
    g.name,
    COUNT(*)
FROM genres g
JOIN show_genres sg ON sg.genre_id = g.genre_id
GROUP BY g.name;


-- After index

EXPLAIN ANALYZE
SELECT
    g.name,
    COUNT(*)
FROM genres g
JOIN show_genres sg ON sg.genre_id = g.genre_id
GROUP BY g.name;
