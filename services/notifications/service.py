from enum import Enum
from typing import Union

import requests
from pydantic import BaseModel

from rabbitmq.types import StateUpdatedMessage


class NotificationType(str, Enum):
    STATE = "state"


class NotificationMessage(BaseModel):
    type: NotificationType
    message: Union[
        StateUpdatedMessage
    ]


class NotificationService:
    def __init__(self) -> None:
        self.notification_urls = {}

    def subscribe(self, client: str, url: str) -> None:
        self.notification_urls[client] = url

    def unsubscribe(self, client: str) -> None:
        if client in self.notification_urls:
            del self.notification_urls[client]

    def send_notification(self, message: NotificationMessage) -> None:
        for client_ip, url in self.notification_urls.items():
            requests.post(url, json=message)
