from fastapi import APIRouter, Request

from routers.notifications.types import NotificationSubscribeRequest
from services.notifications import notification_service

router = APIRouter(
    prefix="/notifications",
    tags=["notifications"]
)


@router.post("/subscribe")
async def notifications_subscribe(body: NotificationSubscribeRequest, request: Request):
    notification_url = body.notification_url
    client = f"{request.client.host}:{request.client.port}"

    notification_service.subscribe(client, notification_url)


@router.post("/unsubscribe")
async def notifications_unsubscribe(request: Request):
    client = f"{request.client.host}:{request.client.port}"
    notification_service.unsubscribe(client)


# temporary
@router.get("/")
async def notifications_get():
    return notification_service.notification_urls
