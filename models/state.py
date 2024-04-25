from enum import Enum
from typing import Union

from pydantic import BaseModel

from services.actions.types import HSLAColor


class Status(str, Enum):
    online = "online"
    offline = "offline"


class ColorLightMode(str, Enum):
    Color = "color"
    White = "white"


class ColorLightState(BaseModel):
    status: Status
    mode: ColorLightMode
    color: HSLAColor
    temperature: int
    brightness: int


class AirConditionerMode(str, Enum):
    Automatic = "automatic"
    Cooling = "cooling"
    Heating = "heating"


class AirConditionerState(BaseModel):
    status: Status
    mode: AirConditionerMode
    current_temperature: int
    current_threshold_temperature: int


class TelevisionState(BaseModel):
    status: Status
    channel: int


State = Union[
    AirConditionerState,
    ColorLightState,
    TelevisionState,
]
