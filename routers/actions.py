from fastapi import APIRouter

from errors.models import HAUTOError
from services import action

router = APIRouter(
    prefix="/actions/{device_id}"
)


@router.post("/turn_on")
async def turn_on(device_id: int):
    try:
        await action.turn_on(device_id)
    except Exception as e:
        print(e)
        raise HAUTOError(501, "Action is not implemented")


@router.post("/turn_off")
async def turn_off(device_id: int):
    try:
        await action.turn_off(device_id)
    except Exception as e:
        print(e)
        raise HAUTOError(501, "Action is not implemented")


@router.post("/set_rgb_color")
async def set_rgb_color(device_id: int, body: dict):
    raise HAUTOError(501, "Action is not implemented")
