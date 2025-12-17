from fastapi import APIRouter, HTTPException
from api.schemas import ShowIngestPayload
from api.validators import parse_duration, validate_type
from api.db import get_conn
from api import repository as repo

router = APIRouter()

@router.post("/ingest/show")
def ingest_show(payload: ShowIngestPayload):
    try:
        validate_type(payload.type)
        duration_value, duration_unit = parse_duration(payload.duration)
    except ValueError as e:
        raise HTTPException(status_code=400, detail=str(e))

    try:
        with get_conn() as conn:
            rating_id = repo.get_rating_id(conn, payload.rating)

            with conn.cursor() as cur:
                cur.execute(
                    """
                    INSERT INTO shows (
                        show_id, type, title, description,
                        release_year, date_added,
                        duration_value, duration_unit, rating_id
                    )
                    VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s)
                    ON CONFLICT (show_id) DO NOTHING
                    """,
                    (
                        payload.show_id,
                        payload.type,
                        payload.title,
                        payload.description,
                        payload.release_year,
                        payload.date_added,
                        duration_value,
                        duration_unit,
                        rating_id,
                    )
                )

            for genre in payload.genres:
                genre_id = repo.ensure_genre(conn, genre)
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO show_genres (show_id, genre_id)
                        VALUES (%s,%s)
                        ON CONFLICT DO NOTHING
                        """,
                        (payload.show_id, genre_id)
                    )

            for country in payload.countries:
                country_id = repo.ensure_country(conn, country)
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO show_countries (show_id, country_id)
                        VALUES (%s,%s)
                        ON CONFLICT DO NOTHING
                        """,
                        (payload.show_id, country_id)
                    )

            for actor in payload.people.actors:
                pid = repo.ensure_person(conn, actor)
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO show_people (show_id, person_id, role)
                        VALUES (%s,%s,'actor')
                        ON CONFLICT DO NOTHING
                        """,
                        (payload.show_id, pid)
                    )

            for director in payload.people.directors:
                pid = repo.ensure_person(conn, director)
                with conn.cursor() as cur:
                    cur.execute(
                        """
                        INSERT INTO show_people (show_id, person_id, role)
                        VALUES (%s,%s,'director')
                        ON CONFLICT DO NOTHING
                        """,
                        (payload.show_id, pid)
                    )

    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

    return {"status": "inserted"}
