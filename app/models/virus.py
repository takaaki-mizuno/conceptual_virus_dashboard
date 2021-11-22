from sqlalchemy import BigInteger, Column, String

from .base import Base


class Virus(Base):
    __tablename__ = 'viruses'
    id = Column(BigInteger, primary_key=True)
    hash = Column(String, nullable=False)
    code = Column(String, nullable=False)
