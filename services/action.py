from clients.rabbitmq.publications import action_request


async def turn_on(device_id: int):
    message = {"device_id": device_id}
    await action_request("turn_on", message)


async def turn_off(device_id: int):
    message = {"device_id": device_id}
    await action_request("turn_off", message)