from typing import Dict, Any

from pydantic import BaseModel


class Device(BaseModel):
    id: int
    natural_id: str
    name: str
    manufacturer: str | None = None
    model: str | None = None
    room_id: int
    controller: str


class DeviceState(BaseModel):
    device_id: int
    timestamp: str
    state: Dict[str, Any]


# Errors
class DeviceNotFoundError(Exception):
    pass


class DeviceStateNotFoundError(Exception):
    pass
