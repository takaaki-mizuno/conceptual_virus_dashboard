from typing import List

from pydantic import BaseModel

from .virus import Virus


class StatusUpdate(BaseModel):
    ip_address: str
    identity_key: str
    status: List[Virus]
