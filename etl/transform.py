VALID_RATINGS = {
    "G", "PG", "PG-13", "R", "NC-17",
    "TV-Y", "TV-Y7", "TV-Y7-FV", "TV-G",
    "TV-PG", "TV-14", "TV-MA",
    "NR", "UR"
}

def transform_ratings(rows):
    """
    Extract valid, unique ratings from staging rows.
    Invalid or unexpected values are ignored.
    """
    ratings = set()
    rejected = set()

    for row in rows:
        value = row["rating"]

        if not value:
            continue

        if value in VALID_RATINGS:
            ratings.add(value)
        else:
            rejected.add(value)

    return ratings, rejected

def normalize_genre(value: str) -> str:
    value = value.strip()

    # Title case first
    value = value.title()

    # Fix common acronyms
    value = value.replace("Tv ", "TV ")
    value = value.replace("Tv&", "TV&")
    value = value.replace(" Tv", " TV")

    return value

def transform_genres(rows):
    """
    Transform listed_in into genres and show-genre relationships.
    """
    genres = set()
    show_genres = []
    rejected = set()

    for row in rows:
        show_id = row["show_id"]
        raw = row["listed_in"]

        if not raw:
            continue

        parts = raw.split(",")

        for part in parts:
            genre = normalize_genre(part)

            if not genre:
                rejected.add(part)
                continue

            genres.add(genre)
            show_genres.append((show_id, genre))

    return genres, show_genres, rejected


def parse_duration(value: str):
    """
    Parse duration string into (duration_value, duration_unit).
    Examples:
      '90 min'     -> (90, 'minutes')
      '3 Seasons'  -> (3, 'seasons')
    """
    if not value:
        return None, None

    value = value.strip().lower()

    try:
        number = int(value.split()[0])
    except (ValueError, IndexError):
        return None, None

    if "min" in value:
        return number, "minutes"
    if "season" in value:
        return number, "seasons"

    return None, None

def transform_shows(rows, rating_map):
    shows = []

    for row in rows:
        rating_code = row["rating"]
        rating_id = rating_map.get(rating_code)

        duration_value, duration_unit = parse_duration(row["duration"])

        shows.append({
            "show_id": row["show_id"],
            "type": row["type"],
            "title": row["title"],
            "description": row["description"],
            "release_year": row["release_year"],
            "date_added": row["date_added"],
            "duration_value": duration_value,
            "duration_unit": duration_unit,
            "rating_id": rating_id,  # may be None
        })

    return shows



def normalize_country(value: str) -> str:
    return value.strip().title()

def transform_countries(rows):
    """
    Transform country column into countries and show-country relationships.
    """
    countries = set()
    show_countries = []
    rejected = set()

    for row in rows:
        show_id = row["show_id"]
        raw = row["country"]

        if not raw:
            continue

        parts = raw.split(",")

        for part in parts:
            country = normalize_country(part)

            if not country:
                rejected.add(part)
                continue

            countries.add(country)
            show_countries.append((show_id, country))

    return countries, show_countries, rejected



def normalize_person(name: str) -> str:
    return name.strip()

def transform_people(rows):
    """
    Extract people and role-based relationships.
    """
    people = set()
    show_people = []
    rejected = set()

    for row in rows:
        show_id = row["show_id"]

        # Directors
        if row["director"]:
            directors = row["director"].split(",")
            for d in directors:
                name = normalize_person(d)
                if not name:
                    rejected.add(d)
                    continue
                people.add(name)
                show_people.append((show_id, name, "director"))

        # Cast / actors
        if row["cast_members"]:
            actors = row["cast_members"].split(",")
            for a in actors:
                name = normalize_person(a)
                if not name:
                    rejected.add(a)
                    continue
                people.add(name)
                show_people.append((show_id, name, "actor"))

    return people, show_people, rejected













