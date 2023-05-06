import secrets
from app.logging.logger import log
from fastapi import APIRouter
from app.schemas.requests import UrlToBeShorted, UrlToBeDeleted
from app.schemas.responses import ShortedResponse
from app.utils.redis_handler import get_redis_handler
from typing import List, Dict

router = APIRouter(prefix="/shrt", tags=["shortie"])


Redis = get_redis_handler()


@router.post("/", status_code=200)
async def short(param: UrlToBeShorted) -> ShortedResponse:
    """returns data about shorted url"""
    key = secrets.token_hex(nbytes=4)
    Redis.put(key, param.url, 15)
    return {"key": key, "surl": f"http://localhost:7000/s/{key}"}



@router.get("/all")
def get_all_values(pattern: str | None = None) -> List[Dict[str, str]]: #TODO: refactor when user is implemented
    if pattern:
        return Redis.all(pattern)
    return Redis.all()

@router.delete("/")
def remove_shorted(body: UrlToBeDeleted):
    Redis.remove(body.hash, "mamprava")
    return "ok"

