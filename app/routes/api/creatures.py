from database import get_db
from fastapi import APIRouter, Depends, Query
from sqlalchemy.orm import Session

api_creatures = APIRouter()


@api_creatures.post("/status", summary="Update creature status")
async def status(db: Session = Depends(get_db)):
    pass
