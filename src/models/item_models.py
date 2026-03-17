from dataclasses import dataclass
from uuid import UUID


@dataclass
class ItemDBDTO:
    id: int
    type: str
    icon_path: str
    name: str
    description: str


@dataclass
class UserItemDBDTO(ItemDBDTO):
    user_uuid: UUID


@dataclass
class Item:
    id: int
    type: str
    icon_path: str
    name: str
    description: str


@dataclass
class UserItem(Item):
    user_uuid: UUID
