def insert_ratings(conn, ratings):
    """
    Insert ratings into ratings table.
    """
    with conn.cursor() as cur:
        for code in ratings:
            cur.execute(
                """
                INSERT INTO ratings (code)
                VALUES (%s)
                ON CONFLICT (code) DO NOTHING
                """,
                (code,)
            )
    conn.commit()



def insert_genres(conn, genres):
    with conn.cursor() as cur:
        for name in genres:
            cur.execute(
                """
                INSERT INTO genres (name)
                VALUES (%s)
                ON CONFLICT (name) DO NOTHING
                """,
                (name,)
            )
    conn.commit()

def fetch_genre_map(conn):
    """
    Returns { genre_name: genre_id }
    """
    with conn.cursor() as cur:
        cur.execute("SELECT genre_id, name FROM genres")
        return {name: gid for gid, name in cur.fetchall()}

def insert_show_genres(conn, show_genres, genre_map):
    with conn.cursor() as cur:
        for show_id, genre_name in show_genres:
            genre_id = genre_map.get(genre_name)
            if not genre_id:
                continue

            cur.execute(
                """
                INSERT INTO show_genres (show_id, genre_id)
                VALUES (%s, %s)
                ON CONFLICT DO NOTHING
                """,
                (show_id, genre_id)
            )
    conn.commit()



def insert_shows(conn, shows):
    with conn.cursor() as cur:
        for show in shows:
            cur.execute(
                """
                INSERT INTO shows (
                    show_id,
                    type,
                    title,
                    description,
                    release_year,
                    date_added,
                    duration_value,
                    duration_unit,
                    rating_id
                )
                VALUES (
                    %(show_id)s,
                    %(type)s,
                    %(title)s,
                    %(description)s,
                    %(release_year)s,
                    %(date_added)s,
                    %(duration_value)s,
                    %(duration_unit)s,
                    %(rating_id)s
                )
                ON CONFLICT (show_id) DO NOTHING
                """,
                show
            )
    conn.commit()



def insert_countries(conn, countries):
    with conn.cursor() as cur:
        for name in countries:
            cur.execute(
                """
                INSERT INTO countries (name)
                VALUES (%s)
                ON CONFLICT (name) DO NOTHING
                """,
                (name,)
            )
    conn.commit()

def fetch_country_map(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT country_id, name FROM countries")
        return {name: cid for cid, name in cur.fetchall()}

def insert_show_countries(conn, show_countries, country_map):
    with conn.cursor() as cur:
        for show_id, country_name in show_countries:
            country_id = country_map.get(country_name)
            if not country_id:
                continue

            cur.execute(
                """
                INSERT INTO show_countries (show_id, country_id)
                VALUES (%s, %s)
                ON CONFLICT DO NOTHING
                """,
                (show_id, country_id)
            )
    conn.commit()



def insert_people(conn, people):
    with conn.cursor() as cur:
        for name in people:
            cur.execute(
                """
                INSERT INTO people (name)
                VALUES (%s)
                ON CONFLICT (name) DO NOTHING
                """,
                (name,)
            )
    conn.commit()

def fetch_person_map(conn):
    with conn.cursor() as cur:
        cur.execute("SELECT person_id, name FROM people")
        return {name: pid for pid, name in cur.fetchall()}

def insert_show_people(conn, show_people, person_map):
    with conn.cursor() as cur:
        for show_id, person_name, role in show_people:
            person_id = person_map.get(person_name)
            if not person_id:
                continue

            cur.execute(
                """
                INSERT INTO show_people (show_id, person_id, role)
                VALUES (%s, %s, %s)
                ON CONFLICT DO NOTHING
                """,
                (show_id, person_id, role)
            )
    conn.commit()
