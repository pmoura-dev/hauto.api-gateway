from fastapi import status, APIRouter

from errors import HAUTOAPIErrorResponse, HAUTOAPIError
from rabbitmq.publisher import RabbitMQPublisher
from routers.actions.types import callback_url_param, ActionAcceptedResponse
from services.actions.service import ActionService
from services.actions.types import HSLAColor

router = APIRouter(
    prefix="/devices/{device_id}/actions",
    responses={
        status.HTTP_202_ACCEPTED: {'description': 'Accepted', 'model': ActionAcceptedResponse},
        status.HTTP_500_INTERNAL_SERVER_ERROR: {'model': HAUTOAPIErrorResponse}
    },
    tags=["actions"]
)

action_service = ActionService(RabbitMQPublisher())


@router.post("/turn_on", status_code=status.HTTP_202_ACCEPTED)
async def turn_on(device_id: int, callback_url: str = callback_url_param):
    try:
        correlation_id = await action_service.turn_on(device_id, callback_url)
        return ActionAcceptedResponse(correlation_id=correlation_id)
    except Exception as e:
        raise HAUTOAPIError(str(e))


@router.post("/turn_off", status_code=status.HTTP_202_ACCEPTED)
async def turn_off(device_id: int, callback_url: str = callback_url_param):
    try:
        correlation_id = await action_service.turn_off(device_id, callback_url)
        return ActionAcceptedResponse(correlation_id=correlation_id)
    except Exception as e:
        raise HAUTOAPIError(str(e))


@router.post("/set_color", status_code=status.HTTP_202_ACCEPTED)
async def set_color(device_id: int, color: HSLAColor, callback_url: str = callback_url_param):
    try:
        correlation_id = await action_service.set_color(device_id, color, callback_url)
        return ActionAcceptedResponse(correlation_id=correlation_id)
    except Exception as e:
        raise HAUTOAPIError(str(e))
