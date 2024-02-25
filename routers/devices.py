import logging
from typing import List

from fastapi import APIRouter
from starlette import status

import services.devices.service as devices_service
from errors.models import HAUTOErrorResponse, HAUTOError
from services.devices.types import DeviceStateNotFoundError, DeviceState, Device, DeviceNotFoundError

router = APIRouter(
    prefix="/devices",
    tags=["Device Management"]
)


@router.get("/{device_id}", responses={
    status.HTTP_200_OK: {"model": Device},
    status.HTTP_404_NOT_FOUND: {"model": HAUTOErrorResponse},
    status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": HAUTOErrorResponse}
})
async def get_device(device_id: int) -> Device:
    try:
        return devices_service.get_device(device_id)
    except DeviceNotFoundError:
        raise HAUTOError(code=status.HTTP_404_NOT_FOUND, message="Device not found")
    except Exception as e:
        logging.info(e)
        raise HAUTOError(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message="Internal Server Error")


@router.get("/", responses={
    status.HTTP_200_OK: {"model": List[Device]},
    status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": HAUTOErrorResponse}
})
async def list_devices() -> List[Device]:
    try:
        raise NotImplemented
    except Exception as e:
        logging.info(e)
        raise HAUTOError(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message="Internal Server Error")


@router.get("/{device_id}/state", responses={
    status.HTTP_200_OK: {"model": DeviceState},
    status.HTTP_404_NOT_FOUND: {"model": HAUTOErrorResponse},
    status.HTTP_500_INTERNAL_SERVER_ERROR: {"model": HAUTOErrorResponse}
})
async def get_device_state(device_id: int) -> DeviceState:
    try:
        return devices_service.get_device_state(device_id)
    except DeviceStateNotFoundError:
        raise HAUTOError(code=status.HTTP_404_NOT_FOUND, message="Device state not found")
    except Exception as e:
        logging.info(e)
        raise HAUTOError(code=status.HTTP_500_INTERNAL_SERVER_ERROR, message="Internal Server Error")
