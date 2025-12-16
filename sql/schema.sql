CREATE TABLE ratings (
    rating_id SERIAL PRIMARY KEY,
    code TEXT UNIQUE NOT NULL
);

CREATE TABLE genres (
    genre_id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE countries (
    country_id SERIAL PRIMARY KEY,
    name TEXT UNIQUE NOT NULL
);

CREATE TABLE people (
    person_id SERIAL PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE shows (
    show_id TEXT PRIMARY KEY,
    type TEXT CHECK (type IN ('Movie', 'TV Show')),
    title TEXT NOT NULL,
    description TEXT,
    release_year INTEGER,
    date_added DATE,
    duration_value INTEGER,
    duration_unit TEXT CHECK (duration_unit IN ('minutes', 'seasons')),
    rating_id INTEGER REFERENCES ratings(rating_id)
);

CREATE TABLE show_people (
    show_id TEXT REFERENCES shows(show_id) ON DELETE CASCADE,
    person_id INTEGER REFERENCES people(person_id) ON DELETE CASCADE,
    role TEXT CHECK (role IN ('actor', 'director')),
    PRIMARY KEY (show_id, person_id, role)
);

CREATE TABLE show_genres (
    show_id TEXT REFERENCES shows(show_id) ON DELETE CASCADE,
    genre_id INTEGER REFERENCES genres(genre_id) ON DELETE CASCADE,
    PRIMARY KEY (show_id, genre_id)
);

CREATE TABLE show_countries (
    show_id TEXT REFERENCES shows(show_id) ON DELETE CASCADE,
    country_id INTEGER REFERENCES countries(country_id) ON DELETE CASCADE,
    PRIMARY KEY (show_id, country_id)
);






















