from app.services.default_service import DefaultService
from fastapi import APIRouter


router = APIRouter()


@router.get("/ping")
async def ping() -> str:
    return "pong"


@router.get("/version")
async def get_app_version() -> str:
    return DefaultService().get_version()


@router.get("/status")
async def get_app_status() -> str:
    return await DefaultService().get_status()
