from enum import Enum


class BrokerEventType(Enum):
    USER_REGISTRATION = "user-registration"
    COLLECTED_REWARD = "collection_reward"
