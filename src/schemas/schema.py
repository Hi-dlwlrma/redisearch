from pydantic import BaseModel


class Request(BaseModel):
    id: str
    name: str
