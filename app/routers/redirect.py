from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse 
from app.utils.redis_handler import get_redis_handler

router = APIRouter(prefix="/s", tags=["redirect"])

Redis = get_redis_handler()


@router.get("/{url_key}")
def forward_to_target_url(url_key: str):
    url = Redis.get(url_key)
    if url:
        return RedirectResponse(url.decode("utf-8"))
    raise HTTPException(status_code=404, detail="Item not found")
