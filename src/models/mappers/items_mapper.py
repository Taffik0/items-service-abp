from src.models.item_models import Item, ItemDBDTO, UserItem, UserItemDBDTO


def item_dbdto_to_dto(item_db: ItemDBDTO) -> Item:
    return Item(
        id=item_db.id,
        type=item_db.type,
        icon_path=item_db.icon_path,
        name=item_db.name,
        description=item_db.description)


def user_item_dbdto_to_dto(user_item_db: UserItemDBDTO) -> UserItem:
    return UserItem(
        id=user_item_db.id,
        type=user_item_db.type,
        icon_path=user_item_db.icon_path,
        name=user_item_db.name,
        description=user_item_db.description,
        user_uuid=user_item_db.user_uuid)
