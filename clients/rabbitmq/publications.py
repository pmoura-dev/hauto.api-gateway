from clients.rabbitmq import client


async def action_request(action: str, message: dict):
    await client.publish(
        message=message,
        topic=f"{action}.action",
        exchange="devices"
    )
