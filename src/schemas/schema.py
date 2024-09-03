from pydantic import BaseModel
from typing import List


class Movie(BaseModel):
    id: str
    title: str
    director: str
    genres: List[str]
    overview: str
    vote_average: float
    vote_count: int
