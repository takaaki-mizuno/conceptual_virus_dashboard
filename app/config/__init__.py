import os
from typing import Optional, Union

from pydantic import AnyHttpUrl, BaseSettings, IPvAnyAddress


class Config(BaseSettings):
    DB_USERNAME: str = os.getenv("DB_USERNAME", "postgres")
    DB_PASSWORD: str = os.getenv("DB_PASSWORD", "")
    DB_HOST: Union[AnyHttpUrl,
                   IPvAnyAddress] = os.getenv("DB_HOST", "127.0.0.1")
    DB_NAME: str = 'conceptual_virus'

    SQLALCHEMY_DATABASE_URI = f"postgresql://{{DB_USERNAME}}:{{DB_PASSWORD}}@{{DB_HOST}}/{{DB_NAME}}"


config = Config()
