# api/validators.py

ALLOWED_TYPES = {"Movie", "TV Show"}

def validate_type(show_type: str):
    if show_type not in ALLOWED_TYPES:
        raise ValueError("Invalid show type")


def parse_duration(duration: str) -> tuple[int, str]:
    parts = duration.strip().lower().split()

    if len(parts) != 2:
        raise ValueError("Invalid duration format")

    value_str, unit = parts

    if not value_str.isdigit():
        raise ValueError("Duration value must be an integer")

    value = int(value_str)

    if unit.startswith("min"):
        return value, "minutes"
    if unit.startswith("season"):
        return value, "seasons"

    raise ValueError("Invalid duration unit")
