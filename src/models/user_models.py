from pydantic import BaseModel


class CreateUser(BaseModel):
    uuid: str
    type: str

    class Config:
        extra = "ignore"
