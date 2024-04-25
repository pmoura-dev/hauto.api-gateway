from datetime import datetime
from typing import Optional, Annotated, Union

from faststream.broker.fastapi.context import Context
from pydantic import BaseModel

from models.state import ColorLightState, AirConditionerState, TelevisionState

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


class StateUpdatedMessage(BaseModel):
    device_id: int
    timestamp: datetime
    state: Union[
        AirConditionerState,
        ColorLightState,
        TelevisionState
    ]
