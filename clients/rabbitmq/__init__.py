import os

from faststream.rabbit import RabbitBroker


class Client:

    def __init__(self, url):
        self.url = url

    async def publish(self, message: dict, topic: str, exchange: str):
        async with RabbitBroker(self.url) as broker:
            await broker.publish(message=message, exchange=exchange, routing_key=topic)


client = Client(os.environ.get("rabbitmq_host"))
