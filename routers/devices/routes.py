from typing import List

from fastapi import APIRouter
from starlette import status

from clients import transaction_service
from errors import HAUTOAPIErrorResponse, HAUTOAPIError
from models.devices import DeviceDetails
from services.devices.service import DeviceService

router = APIRouter(
    prefix="/devices",
    tags=["devices"],
)

device_service = DeviceService(transaction_service.Client())


@router.get("/details",
            responses={
                status.HTTP_200_OK: {'model': List[DeviceDetails]},
                status.HTTP_500_INTERNAL_SERVER_ERROR: {'model': HAUTOAPIErrorResponse}
            })
async def get_devices_details() -> List[DeviceDetails]:
    try:
        return device_service.get_all_device_details()
    except Exception as e:
        raise HAUTOAPIError(str(e))
