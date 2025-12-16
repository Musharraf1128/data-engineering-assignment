CREATE OR REPLACE FUNCTION get_shows_by_genre(genre_name TEXT)
RETURNS TABLE (
    title TEXT,
    type TEXT,
    release_year INT,
    genre TEXT
) AS $$
BEGIN
    RETURN QUERY
    SELECT
        s.title,
        s.type,
        s.release_year,
        g.name
    FROM shows s
    JOIN show_genres sg ON sg.show_id = s.show_id
    JOIN genres g ON g.genre_id = sg.genre_id
    WHERE g.name ILIKE '%' || genre_name || '%';
END;
$$ LANGUAGE plpgsql;
