from fastapi import FastAPI
from routes.api import api_creatures, api_dashboard


def create_app():
    app = FastAPI(title="Conceptual Virus Dashboard", )

    app.include_router(
        api_creatures,
        prefix="/api/creatures",
    )

    app.include_router(
        api_dashboard,
        prefix="/api/dashboard",
    )

    return app
