from pydantic import BaseModel


class NotificationSubscribeRequest(BaseModel):
    notification_url: str
