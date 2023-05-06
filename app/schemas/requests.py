from pydantic import BaseModel
from typing import Optional


class UrlToBeShorted(BaseModel):
    url: str

class UrlToBeDeleted(BaseModel):
    hash: str

class RegisterSchema(BaseModel):
    username: str
    email: str
    profileslug: str
    password: str


class LoginSchema(BaseModel):
    username: str
    password: str


class UserUpdateBody(BaseModel):
    username: Optional[str]
    email: Optional[str]