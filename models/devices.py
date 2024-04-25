from typing import Optional

from pydantic import BaseModel

from models.state import State


class DeviceDetails(BaseModel):
    id: int
    natural_id: str
    name: str
    room: str
    type: str
    controller: str
    state: Optional[State] = None
