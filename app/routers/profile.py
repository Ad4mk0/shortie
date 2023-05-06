import secrets
from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse 
from app.utils.redis_handler import get_redis_handler
from app.schemas.requests import RegisterSchema, LoginSchema, UrlToBeShorted

router = APIRouter(prefix="/profile", tags=["profile"])

Redis = get_redis_handler()


@router.post("/register")
def register(body: RegisterSchema):
    #TODO: do some freaky shit here
    return "ok"


@router.post("/login")
def login(body: LoginSchema):
    return "logged ok"



@router.get("/p/{profile_hash}")
def login(profile_hash: str):
    return {
        "userName": "The Old Mighty",
        "avatar": "someavatar",
        "links": [
            {"key": "val"},
            {"key": "val"},
            {"key": "val"}
        ]
    }


@router.post("/{idx}", status_code=200)
def add_shorted_link(idx: int, param: UrlToBeShorted):
    #TODO: get profile slug
    slug = "SOME_SLUG"
    key = secrets.token_hex(nbytes=4)
    Redis.put_slug(key, slug, param.url)
    return "ok"


@router.delete("/{idx}")
def user_delete():
    "this will delete some url for user"
    pass


@router.get("/{idx}")
def user_get():
    "This will get all the links for given user"
    pass

@router.post("/{idx}")
def user_modify():
    "This will modify some url for given user"
    pass