from pydantic import BaseModel


class Virus(BaseModel):
    index: int
    life_time: int
    length: int
    hash: str
