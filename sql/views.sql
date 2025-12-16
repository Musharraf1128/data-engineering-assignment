CREATE VIEW vw_show_full_metadata AS
SELECT
    s.show_id,
    s.title,
    s.type,
    r.code AS rating,
    s.release_year,
    STRING_AGG(DISTINCT g.name, ', ') AS genres,
    STRING_AGG(DISTINCT c.name, ', ') AS countries
FROM shows s
LEFT JOIN ratings r ON r.rating_id = s.rating_id
LEFT JOIN show_genres sg ON sg.show_id = s.show_id
LEFT JOIN genres g ON g.genre_id = sg.genre_id
LEFT JOIN show_countries sc ON sc.show_id = s.show_id
LEFT JOIN countries c ON c.country_id = sc.country_id
GROUP BY s.show_id, r.code;
