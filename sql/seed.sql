-- Ratings
INSERT INTO ratings (code) VALUES
('G'),
('PG'),
('PG-13'),
('R'),
('TV-Y'),
('TV-Y7'),
('TV-G'),
('TV-PG'),
('TV-14'),
('TV-MA')
ON CONFLICT (code) DO NOTHING;

-- Genres
INSERT INTO genres (name) VALUES
('Action'),
('Adventure'),
('Anime'),
('Children'),
('Comedy'),
('Crime'),
('Documentary'),
('Drama'),
('Fantasy'),
('Horror'),
('International Movies'),
('Romance'),
('Sci-Fi'),
('Thriller'),
('TV Shows')
ON CONFLICT (name) DO NOTHING;

-- Countries (partial seed;can be extended this)
INSERT INTO countries (name) VALUES
('United States'),
('India'),
('United Kingdom'),
('Canada'),
('France'),
('Germany'),
('Japan'),
('South Korea')
ON CONFLICT (name) DO NOTHING;
