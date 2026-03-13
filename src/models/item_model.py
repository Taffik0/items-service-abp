from pydantic import BaseModel


class CollectionReward(BaseModel):
    type: str
    id: int
    user_uuid: str
