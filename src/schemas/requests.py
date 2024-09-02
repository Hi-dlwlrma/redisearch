from pydantic import BaseModel


class Request(BaseModel):
    id: int
    value: str
