from typing import Optional

from messaging.types import Message
from rabbitmq.router import router


class RabbitMQPublisher:

    def __init__(self):
        self.broker = router.broker

    async def publish(self, topic: str, message: Message, extras: Optional[dict] = None) -> None:
        await self.broker.publish(
            exchange=extras["exchange"],
            routing_key=topic,
            correlation_id=message.meta.correlation_id,
            message=message.model_dump_json(exclude_none=True)
        )
