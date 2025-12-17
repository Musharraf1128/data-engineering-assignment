from psycopg import Connection

def get_rating_id(conn: Connection, code: str | None) -> int | None:
    if not code:
        return None

    with conn.cursor() as cur:
        cur.execute(
            "SELECT rating_id FROM ratings WHERE code = %s",
            (code,)
        )
        row = cur.fetchone()
        return row[0] if row else None


def ensure_genre(conn: Connection, name: str) -> int:
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO genres (name)
            VALUES (%s)
            ON CONFLICT (name) DO NOTHING
            """,
            (name,)
        )
        cur.execute(
            "SELECT genre_id FROM genres WHERE name = %s",
            (name,)
        )
        return cur.fetchone()[0]


def ensure_country(conn: Connection, name: str) -> int:
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO countries (name)
            VALUES (%s)
            ON CONFLICT (name) DO NOTHING
            """,
            (name,)
        )
        cur.execute(
            "SELECT country_id FROM countries WHERE name = %s",
            (name,)
        )
        return cur.fetchone()[0]


def ensure_person(conn: Connection, name: str) -> int:
    with conn.cursor() as cur:
        cur.execute(
            """
            INSERT INTO people (name)
            VALUES (%s)
            ON CONFLICT (name) DO NOTHING
            """,
            (name,)
        )
        cur.execute(
            "SELECT person_id FROM people WHERE name = %s",
            (name,)
        )
        return cur.fetchone()[0]
