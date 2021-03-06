import logging

from fastapi import APIRouter, Body, Depends
from fastapi import status as status_code
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

from ....api.requests import StatusUpdate
from ....database import get_db
from ....services import CreatureService


api_creatures = APIRouter()
logger = logging.getLogger(__name__)


@api_creatures.post("/status", summary="Update creature status")
async def status(
        db: Session = Depends(get_db), *, status_update: StatusUpdate):
    service = CreatureService()
    _status = []
    for virus in status_update.s:
        _status.append(virus.dict())

    _creature, _snapshot = service.register_creature(db, status_update.i,
                                                     status_update.k, _status)

    return JSONResponse(status_code=status_code.HTTP_200_OK, content={"status": "ok"})
