from datetime import datetime
from enum import Enum
from typing import Optional, Annotated, Union

from faststream.broker.fastapi.context import Context
from pydantic import BaseModel

from services.actions.types import HSLAColor

DEVICES_EXCHANGE = "devices"

ACTION_SUCCESSES_QUEUE = "action.successes.api-gateway.queue"
ACTION_FAILURES_QUEUE = "action.failures.api-gateway.queue"
STATE_UPDATES_QUEUE = "state.updates.api-gateway.queue"

ACTION_SUCCEEDED_TOPIC = "action.succeeded"
ACTION_FAILED_TOPIC = "action.failed"
STATE_UPDATED_TOPIC = "state.updated"

CorrelationID = Annotated[str, Context("message.correlation_id")]


class ActionSucceededMessage(BaseModel):
    callback_url: Optional[str] = None


class ActionFailedMessage(BaseModel):
    error: Optional[str] = None
    callback_url: Optional[str] = None


# states

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


class StateUpdatedMessage(BaseModel):
    device_id: int
    timestamp: datetime
    state: Union[
        AirConditionerState,
        ColorLightState,
        TelevisionState
    ]
