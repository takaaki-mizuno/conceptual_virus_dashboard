from pydantic import BaseModel


class StatusUpdate(BaseModel):
    ip_address: str
    identity_key: str
