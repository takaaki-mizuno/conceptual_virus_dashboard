from sqlalchemy import JSON, BigInteger, Column, Integer

from .base import Base


class Snapshot(Base):
    __tablename__ = 'snapshots'
    id = Column(BigInteger, primary_key=True)
    creature_id = Column(BigInteger, nullable=False)
    sent_at = Column(Integer, nullable=False)
    status = Column(JSON, nullable=False)
