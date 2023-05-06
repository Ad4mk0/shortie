import secrets
from fastapi import APIRouter, HTTPException
from fastapi.responses import RedirectResponse 
from app.utils.redis_handler import get_redis_handler
from app.schemas.requests import RegisterSchema, LoginSchema, UrlToBeShorted, UserUpdateBody
from app.repository.user import create_user, get_user_by_name_password, get_user_by_slug, user_delete_by_slug, user_update_name_email

router = APIRouter(prefix="/profile", tags=["profile"])

Redis = get_redis_handler()


@router.post("/register")
def register(body: RegisterSchema):
    resp = create_user(body.username, body.email, body.profileslug, body.password)
    if resp:
        return "ok"
    return "nok"


@router.post("/login")
def login(body: LoginSchema):
    try:
        slug = get_user_by_name_password(body.username, body.password)
        if slug:
            return {"slug": slug}
        return HTTPException(status_code=404, detail="Acess denied") 
    except Exception:
        return HTTPException(status_code=404, detail="Acess denied")



@router.get("/p/{slug}")
def profile_infos(slug: str):
    user = get_user_by_slug(slug)
    if user == False:
        return HTTPException(status_code=404, detail="User not found")

    shorted = Redis.get_slug_only(slug)

    return {
        "profile": {
            "username": user.userName,
            "email": user.email,
            "slug": user.profileSlug
        },
        "links": shorted
    }


@router.post("/add/{slug}", status_code=200)
def add_link_to_be_shorted_to_profile(slug: str, param: UrlToBeShorted):
    "Adds link and shorts it to profile"
    user = get_user_by_slug(slug)
    if user == False:
        return HTTPException(status_code=404, detail="User not found")
    
    key = secrets.token_hex(nbytes=4)
    Redis.put_slug(key, slug, param.url)
    return "ok"


@router.delete("/{slug}")
def user_delete(slug: str):
    "Deletes user and its links"
    resp = user_delete_by_slug(slug)
    if resp:
        Redis.remove_slug_only(slug)
        return "ok"
    return HTTPException(status_code=404, detail="User not found")


@router.post("/{slug}")
def user_modify(slug: str, body: UserUpdateBody):
    "This will modify some url for given user"
    resp = user_update_name_email(body.username, body.email)
    if resp:
        return "ok"
    return HTTPException(status_code=404, detail="Something went wrong")
