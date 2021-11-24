from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..api.routes.api import api_creatures, api_dashboard


def create_app():
    app = FastAPI(title="Conceptual Virus Dashboard", )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    app.include_router(
        api_creatures,
        prefix="/api/creatures",
    )

    app.include_router(
        api_dashboard,
        prefix="/api/dashboard",
    )

    return app
