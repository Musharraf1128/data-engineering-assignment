-- Foreign key indexes
CREATE INDEX idx_show_genres_show_id ON show_genres(show_id);
CREATE INDEX idx_show_genres_genre_id ON show_genres(genre_id);

CREATE INDEX idx_show_people_person_id ON show_people(person_id);
CREATE INDEX idx_show_people_role ON show_people(role);

CREATE INDEX idx_show_countries_country_id ON show_countries(country_id);

-- Filtering indexes
CREATE INDEX idx_shows_type ON shows(type);
CREATE INDEX idx_shows_release_year ON shows(release_year);
