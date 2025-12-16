-- Total number of shows by type
SELECT
    type,
    COUNT(*) AS total_shows
FROM shows
GROUP BY type;

-- Average duration of movies (in minutes)
SELECT
    AVG(duration_value) AS avg_movie_duration
FROM shows
WHERE type = 'Movie'
  AND duration_unit = 'minutes';



-- Top 10 genres by number of shows
SELECT
    g.name AS genre,
    COUNT(*) AS total_shows
FROM genres g
JOIN show_genres sg ON sg.genre_id = g.genre_id
GROUP BY g.name
ORDER BY total_shows DESC
LIMIT 10;

-- Countries with most Netflix content
SELECT
    c.name AS country,
    COUNT(*) AS total_shows
FROM countries c
JOIN show_countries sc ON sc.country_id = c.country_id
GROUP BY c.name
ORDER BY total_shows DESC
LIMIT 10;

-- Actors who appeared in the most shows
SELECT
    p.name AS actor,
    COUNT(*) AS appearances
FROM people p
JOIN show_people sp ON sp.person_id = p.person_id
WHERE sp.role = 'actor'
GROUP BY p.name
ORDER BY appearances DESC
LIMIT 10;



-- Shows without a country mapped
SELECT COUNT(*)
FROM shows s
LEFT JOIN show_countries sc ON sc.show_id = s.show_id
WHERE sc.show_id IS NULL;

-- Directors who also acted in the same show
SELECT DISTINCT
    p.name,
    s.title
FROM show_people sp1
JOIN show_people sp2
  ON sp1.show_id = sp2.show_id
 AND sp1.person_id = sp2.person_id
JOIN people p ON p.person_id = sp1.person_id
JOIN shows s ON s.show_id = sp1.show_id
WHERE sp1.role = 'director'
  AND sp2.role = 'actor';






















































