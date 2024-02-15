import json

from faststream import Path
from faststream.rabbit import RabbitQueue, RabbitExchange, ExchangeType
from faststream.rabbit.fastapi import RabbitRouter

import config
from routers.websocket import manager

router = RabbitRouter("amqp://%s:%s@%s:%s/" % (
    config.RABBITMQ_USER,
    config.RABBITMQ_PASSWORD,
    config.RABBITMQ_HOST,
    config.RABBITMQ_PORT
))

devices_exchange = RabbitExchange("devices", durable=True, type=ExchangeType.TOPIC)
state_queue = RabbitQueue("state.api-gateway.queue", auto_delete=True, routing_key="state.{device_id}")


@router.subscriber(state_queue, devices_exchange)
async def state(body: dict, device_id: int = Path()):
    message = {"type": "state", "device_id": device_id, "state": body}
    await manager.broadcast(json.dumps(message))
