VALID_RATINGS = {
    "G", "PG", "PG-13", "R", "NC-17",
    "TV-Y", "TV-Y7", "TV-Y7-FV", "TV-G",
    "TV-PG", "TV-14", "TV-MA",
    "NR", "UR"
}

def is_valid_rating(value: str) -> bool:
    if not value:
        return False
    return value in VALID_RATINGS
