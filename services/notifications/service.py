from typing import Any

import requests


class NotificationService:
    def __init__(self) -> None:
        self.notification_urls = {}

    def subscribe(self, client: str, url: str) -> None:
        self.notification_urls[client] = url

    def unsubscribe(self, client: str) -> None:
        if client in self.notification_urls:
            del self.notification_urls[client]

    def send_notification(self, message: Any) -> None:
        for client_ip, url in self.notification_urls.items():
            requests.post(url, json=message)
