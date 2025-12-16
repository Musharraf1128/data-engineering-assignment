import psycopg
from psycopg.rows import dict_row

def fetch_staging_rows(conn):
    """
    Fetch required columns from staging table.
    Returns list of dicts.
    """
    with conn.cursor(row_factory=dict_row) as cur:
        cur.execute("""
            SELECT
                show_id,
                rating
            FROM staging_netflix_shows
        """)
        return cur.fetchall()
