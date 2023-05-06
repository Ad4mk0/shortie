from pydantic import BaseModel


class UrlToBeShorted(BaseModel):
    url: str

class UrlToBeDeleted(BaseModel):
    hash: str

class RegisterSchema(BaseModel):
    username: str
    email: str
    profileurl: str
    profileslug: str
    password: str


class LoginSchema(BaseModel):
    username: str
    password: str