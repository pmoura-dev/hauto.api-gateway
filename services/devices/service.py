from typing import List

import clients.transaction_service.endpoints as transaction_service
from clients.transaction_service import RecordNotFoundException
from services.devices.types import Device, DeviceState, DeviceNotFoundError, DeviceStateNotFoundError


def get_device(device_id: int) -> Device:
    try:
        response = transaction_service.get_device(device_id)
        return Device(
            id=response["id"],
            natural_id=response["natural_id"],
            name=response["name"],
            manufacturer=response["manufacturer"],
            model=response["model"],
            room_id=response["room_id"],
            controller=response["controller"]
        )
    except RecordNotFoundException:
        raise DeviceNotFoundError


def list_devices() -> List[Device]:
    raise NotImplementedError


def get_device_state(device_id: int) -> DeviceState:
    try:
        response = transaction_service.get_device_state(device_id)

        return DeviceState(
            device_id=response["device_id"],
            timestamp=response["timestamp"],
            state=response["state"]
        )

    except RecordNotFoundException:
        raise DeviceStateNotFoundError
