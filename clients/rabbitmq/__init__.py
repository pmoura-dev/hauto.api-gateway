import os

from faststream.rabbit import RabbitBroker

import config


class Client:

    def __init__(self, host, port, user, password):
        self.url = f'amqp://{user}:{password}@{host}:{port}'

    async def publish(self, message: dict, topic: str, exchange: str):
        async with RabbitBroker(self.url) as broker:
            await broker.publish(message=message, exchange=exchange, routing_key=topic)


client = Client(
    host=config.RABBITMQ_HOST,
    port=config.RABBITMQ_PORT,
    user=config.RABBITMQ_USER,
    password=config.RABBITMQ_PASSWORD
)
