from database import get_db
from fastapi import APIRouter, Depends, Query
from fastapi import status as status_code
from fastapi.responses import JSONResponse
from sqlalchemy.orm import Session

api_dashboard = APIRouter()


@api_dashboard.get("/status", summary="list all creature status")
async def status(db: Session = Depends(get_db)):
    return JSONResponse(status_code=status_code.HTTP_200_OK,
                        content={"status": "ok"})
