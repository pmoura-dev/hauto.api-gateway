from typing import Optional
from uuid import UUID

from messaging.types import Publisher, Metadata
from rabbitmq.types import DEVICES_EXCHANGE
from services.actions.types import TurnOnMessage, TURN_ON_TOPIC, HSLAColor, TurnOffMessage, TURN_OFF_TOPIC, \
    SetColorMessage, SET_COLOR_TOPIC


class ActionService:

    def __init__(self, publisher: Publisher):
        self.publisher: Publisher = publisher

    async def turn_on(self, device_id: int, callback_url: Optional[str] = None) -> UUID:
        message = TurnOnMessage(meta=Metadata(), device_id=device_id, callback_url=callback_url)
        await self.publisher.publish(TURN_ON_TOPIC, message,
                                     extras={"exchange": DEVICES_EXCHANGE})
        return message.meta.correlation_id

    async def turn_off(self, device_id: int, callback_url: Optional[str] = None) -> UUID:
        message = TurnOffMessage(meta=Metadata(), device_id=device_id, callback_url=callback_url)
        await self.publisher.publish(TURN_OFF_TOPIC, message,
                                     extras={"exchange": DEVICES_EXCHANGE})
        return message.meta.correlation_id

    async def set_color(self, device_id: int, color: HSLAColor, callback_url: Optional[str] = None) -> UUID:
        message = SetColorMessage(meta=Metadata(), device_id=device_id, color=color, callback_url=callback_url)
        await self.publisher.publish(SET_COLOR_TOPIC, message,
                                     extras={"exchange": DEVICES_EXCHANGE})
        return message.meta.correlation_id
