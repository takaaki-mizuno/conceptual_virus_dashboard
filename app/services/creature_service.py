import json
import time
from typing import Optional, Tuple

from sqlalchemy import desc
from sqlalchemy.orm import Session

from ..models import Creature, Snapshot, Virus


class CreatureService(object):
    THRESHOLD_DURATION = 60 * 60

    def get_active_creatures(self, db: Session) -> [Creature]:
        current_time = int(time.time())
        threshold_time = current_time - self.THRESHOLD_DURATION
        return db.query(Creature).filter(
            Creature.last_ping_sent_at > threshold_time,
            Creature.is_active == True).all()

    def get_creature(self, db: Session,
                     creature_id: int) -> Optional[Tuple[Creature, Snapshot]]:
        current_time = int(time.time())
        threshold_time = current_time - self.THRESHOLD_DURATION
        creature = db.query(Creature).filter(
            Creature.id == creature_id,
            Creature.last_ping_sent_at > threshold_time,
            Creature.is_active).first()
        if creature is None:
            return None

        snapshot = self.get_snapshot(db, creature_id)
        return creature, snapshot

    def get_snapshot(self, db: Session, creature_id: int) -> Optional[Snapshot]:
        snapshot = db.query(Snapshot).filter(
            Snapshot.creature_id == creature_id).order_by(
            desc(Snapshot.sent_at)).first()

        if snapshot is None:
            return None

        return snapshot

    def register_creature(self, db: Session, ip_address: str,
                          identity_key: str,
                          status: list) -> Optional[Tuple[Creature, Snapshot]]:
        current_time = int(time.time())
        creature = db.query(Creature).filter(
            Creature.ip_address == ip_address,
            Creature.is_active == True).first()
        if creature is not None:
            if creature.identity_key == identity_key:
                db.query(Creature).filter(Creature.id == creature.id).update(
                    {"last_ping_sent_at": current_time})
                db.refresh(creature)
            else:
                db.query(Creature).filter(Creature.id == creature.id).update(
                    {"is_active": False})
                creature = Creature(ip_address=ip_address,
                                    identity_key=identity_key,
                                    last_ping_sent_at=current_time,
                                    first_ping_sent_at=current_time,
                                    is_active=True)
                db.add(creature)
                db.commit()
                db.refresh(creature)
        else:
            creature = Creature(ip_address=ip_address,
                                identity_key=identity_key,
                                last_ping_sent_at=current_time,
                                first_ping_sent_at=current_time,
                                is_active=True)
            db.add(creature)
            db.commit()
            db.refresh(creature)

        snapshot = Snapshot(
            creature_id=creature.id,
            sent_at=current_time,
            status=status,
        )
        db.add(snapshot)
        db.commit()
        db.refresh(snapshot)

        return creature, snapshot

    def get_virus(self, db: Session, _hash: str) -> Virus:
        virus = db.query(Virus).filter(
            Virus.hash == _hash).first()

        return virus

    def set_virus(self, db: Session, _hash: str, sequence: str) -> Virus:
        virus = Virus(hash=_hash, code=sequence)
        db.add(virus)
        db.commit()

        virus = db.query(Virus).filter(
            Virus.hash == _hash).first()

        return virus
