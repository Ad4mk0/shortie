from pydantic import BaseModel


class ShortedResponse(BaseModel):
    key: str
    surl: str
