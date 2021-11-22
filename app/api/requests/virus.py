from pydantic import BaseModel


class Virus(BaseModel):
    i: int
    h: str
