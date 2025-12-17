import psycopg
from psycopg.rows import dict_row

from extract import fetch_staging_rows
from transform import transform_ratings, transform_genres, transform_shows, transform_countries, transform_people
from load import (
    insert_ratings,
    insert_genres,
    fetch_genre_map,
    insert_show_genres,
    insert_shows,
    insert_countries,
    fetch_country_map,
    insert_show_countries,
    insert_people,
    fetch_person_map,
    insert_show_people
)

def main():
    conn = psycopg.connect(
        host="localhost",
        port=5432,
        dbname="netflix_db",
        user="admin",
        password="admin123"
    )

    # RATINGS ETL
    rows = fetch_staging_rows(conn)
    ratings, rejected_ratings = transform_ratings(rows)
    insert_ratings(conn, ratings)

    print(f"Inserted ratings: {sorted(ratings)}")
    print(f"Rejected rating values: {sorted(rejected_ratings)}")

    # GENRES ETL
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("SELECT show_id, listed_in FROM staging_netflix_shows")
        rows = cur.fetchall()

    genres, show_genres, rejected_genres = transform_genres(rows)

    insert_genres(conn, genres)
    genre_map = fetch_genre_map(conn)

    # ---- SHOWS ETL ----
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("""
            SELECT
                show_id,
                type,
                title,
                description,
                release_year,
                duration,
                date_added,
                rating
            FROM staging_netflix_shows
        """)
        show_rows = cur.fetchall()

    rating_map = {
        code: rid
        for rid, code in conn.execute(
            "SELECT rating_id, code FROM ratings"
        ).fetchall()
    }

    shows = transform_shows(show_rows, rating_map)
    insert_shows(conn, shows)

    # COUNTRIES ETL
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("SELECT show_id, country FROM staging_netflix_shows")
        rows = cur.fetchall()

    countries, show_countries, rejected_countries = transform_countries(rows)

    insert_countries(conn, countries)
    country_map = fetch_country_map(conn)
    insert_show_countries(conn, show_countries, country_map)

    print(f"Inserted countries: {len(countries)}")
    print(f"Rejected country values: {rejected_countries}")


    # PEOPLE ETL
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("""
            SELECT show_id, director, cast_members
            FROM staging_netflix_shows
        """)
        rows = cur.fetchall()

    people, show_people, rejected_people = transform_people(rows)

    insert_people(conn, people)
    person_map = fetch_person_map(conn)
    insert_show_people(conn, show_people, person_map)

    print(f"Inserted people: {len(people)}")
    print(f"Rejected people values: {rejected_people}")

    # Relationships

    insert_show_genres(conn, show_genres, genre_map)

    print(f"Inserted genres: {len(genres)}")
    print(f"Rejected genre values: {rejected_genres}")

    conn.close()

if __name__ == "__main__":
    main()
