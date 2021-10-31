from http.routes.api import api_creatures, api_dashboard

from fastapi import FastAPI


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
