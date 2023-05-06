from app.routers import default, shortie, redirect, profile
from app.services.default_service import DefaultService
from fastapi.middleware.cors import CORSMiddleware
from hypercorn.asyncio import serve
from hypercorn.config import Config
import typer
from fastapi import FastAPI, Request, status
from fastapi.exceptions import RequestValidationError
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.utils import get_openapi
from fastapi.responses import JSONResponse
from hypercorn.asyncio import serve
from hypercorn.config import Config
from app.logging.logger import log
import asyncio
import logging

app = typer.Typer()


async def startup_procedures():
    pass
    #TODO: pass


def setup_app() -> FastAPI:
    """Setup FastApi app - configuration, openapi, middleware, routers"""

    fastapi = FastAPI()

    origins = ["*"]

    fastapi.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    fastapi.include_router(default.router)
    fastapi.include_router(shortie.router)
    fastapi.include_router(redirect.router)
    fastapi.include_router(profile.router)


    def custom_openapi():
        if fastapi.openapi_schema:
            return fastapi.openapi_schema
        openapi_schema = get_openapi(
            title="url-shortener",
            version=DefaultService().get_version(),
            description="",
            routes=fastapi.routes,
        )
        fastapi.openapi_schema = openapi_schema
        return fastapi.openapi_schema

    # @fastapi.on_event("startup")
    # async def service_tasks_startup():
    #     """Start all the non-blocking service tasks, which run in the background."""
    #     #get_opc().create()
    #     asyncio.create_task(opcua())

    @fastapi.exception_handler(RequestValidationError)
    async def validation_exception_handler(
        request: Request, exc: RequestValidationError
    ):
        exc_str = f"{exc}".replace("\n", " ").replace("   ", " ")
        log.error(f"{request}: {exc_str}")
        content = {"status_code": 10422, "message": exc_str, "data": None}
        return JSONResponse(
            content=content, status_code=status.HTTP_422_UNPROCESSABLE_ENTITY
        )

    fastapi.openapi = custom_openapi

    return fastapi


@app.command()
def main(config_path: str = "app/configuration.py"):
    asyncio.run(startup_procedures())
    app = setup_app()
    server_config = Config.from_pyfile(config_path)
    log.info("Starting FastApi server!")

    asyncio.run(serve(app, server_config), debug = True)  # type: ignore


if __name__ == "__main__":
    app()
