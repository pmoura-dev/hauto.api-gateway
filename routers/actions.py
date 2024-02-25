from fastapi import APIRouter
from pydantic import BaseModel

from errors.models import HAUTOError
from services import action

router = APIRouter(
    prefix="/devices/{device_id}/action",
    tags=["Actions"]
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


class Temperature(BaseModel):
    value: int


@router.post("/set_heating_threshold_temperature")
async def set_heating_threshold_temperature(device_id: int, temperature: Temperature):
    try:
        await action.set_heating_threshold_temperature(device_id, temperature.value)
    except Exception as e:
        print(e)
        raise HAUTOError(501, "Action is not implemented")


@router.post("/set_cooling_threshold_temperature")
async def set_cooling_threshold_temperature(device_id: int, temperature: Temperature):
    try:
        await action.set_cooling_threshold_temperature(device_id, temperature.value)
    except Exception as e:
        print(e)
        raise HAUTOError(501, "Action is not implemented")


class HeaterCoolerMode(BaseModel):
    mode: str


@router.post("/set_heater_cooler_mode")
async def set_rgb_color(device_id: int, mode: HeaterCoolerMode):
    try:
        await action.set_heater_cooler_mode(device_id, mode.mode)
    except Exception as e:
        print(e)
        raise HAUTOError(501, "Action is not implemented")
