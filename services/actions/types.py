from typing import Optional

from pydantic import BaseModel

from messaging.types import Message

TURN_ON_TOPIC = "action.requested.turn_on"
TURN_OFF_TOPIC = "action.requested.turn_off"
SET_COLOR_TOPIC = "action.requested.set_color"


class ActionMessage(Message):
    device_id: int
    callback_url: Optional[str] = None


class TurnOnMessage(ActionMessage):
    pass


class TurnOffMessage(ActionMessage):
    pass


class HSLAColor(BaseModel):
    hue: int
    saturation: int
    lightness: int
    alpha: Optional[float] = None


class SetColorMessage(ActionMessage):
    color: HSLAColor
