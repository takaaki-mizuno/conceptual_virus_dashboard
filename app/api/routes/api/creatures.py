from api.requests import StatusUpdate
from database import get_db
from fastapi import APIRouter, Depends
from services import CreatureService
from sqlalchemy.orm import Session

api_creatures = APIRouter()


@api_creatures.post("/status", summary="Update creature status")
async def status(
        db: Session = Depends(get_db), *, status_update: StatusUpdate):
    service = CreatureService()
    _creatures, _snapshot = service.register_creature(db, status_update.ip_address, status_update.identity_key,
                                                      status_update.status)
