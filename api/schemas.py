from pydantic import BaseModel, Field
from typing import List, Dict
from datetime import date

class PeoplePayload(BaseModel):
    actors: List[str] = Field(default_factory=list)
    directors: List[str] = Field(default_factory=list)

class ShowIngestPayload(BaseModel):
    show_id: str
    title: str
    type: str
    description: str | None = None
    release_year: int | None = None
    date_added: date | None = None
    duration: str
    rating: str | None = None
    genres: List[str]
    countries: List[str]
    people: PeoplePayload
