from uuid import UUID
from pydantic import BaseModel


class CollectionReward(BaseModel):
    event_id: UUID
    type: str
    id: int
    user_uuid: str
