from sqlalchemy import BigInteger, Boolean, Column, Integer, String

from .base import Base


class Creature(Base):
    __tablename__ = 'creatures'
    id = Column(BigInteger, primary_key=True)
    ip_address = Column(String, nullable=False)
    identity_key = Column(String, nullable=False)
    last_ping_sent_at = Column(Integer, nullable=False)
    first_ping_sent_at = Column(Integer, nullable=False)
    is_active = Column(Boolean, nullable=False)
