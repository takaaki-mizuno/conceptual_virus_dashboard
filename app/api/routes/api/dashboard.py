from database import get_db
from fastapi import APIRouter, Depends, Query
from fastapi import status as status_code
from fastapi.responses import JSONResponse
from services import CreatureService
from sqlalchemy.orm import Session

from ...responses.dashboard import Creature, Creatures, CreatureSummary

api_dashboard = APIRouter()


@api_dashboard.get("/creatures", summary="list all creature status")
async def creatures(db: Session = Depends(get_db)):
    service = CreatureService()
    _creatures = service.get_active_creatures(db)
    response = Creatures(_creatures).to_dict()
    return JSONResponse(status_code=status_code.HTTP_200_OK,
                        content=response)


@api_dashboard.get("/creatures/{creature_id}",
                   summary="list all creature status")
async def creature(db: Session = Depends(get_db), *, creature_id: int):
    service = CreatureService()
    _creature, snapshot = service.get_creature(db, creature_id)
    response = Creature(_creature).to_dict()

    return JSONResponse(status_code=status_code.HTTP_200_OK,
                        content=response)
