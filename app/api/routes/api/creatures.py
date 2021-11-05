from api.requests import StatusUpdate
from database import get_db
from fastapi import APIRouter, Depends
from fastapi import status as status_code
from fastapi.responses import JSONResponse
from services import CreatureService
from sqlalchemy.orm import Session

from ...responses.dashboard import Creature, Creatures, CreatureSummary

api_creatures = APIRouter()


@api_creatures.post("/status", summary="Update creature status")
async def status(
        db: Session = Depends(get_db), *, status_update: StatusUpdate):
    service = CreatureService()
    _status = []
    for virus in status_update.status:
        _status.append(virus.dict())

    _creature, _snapshot = service.register_creature(db, status_update.ip_address, status_update.identity_key,
                                                     _status)

    response = Creature(_creature).to_dict()

    return JSONResponse(status_code=status_code.HTTP_200_OK,
                        content=response)
