from clients.rabbitmq.publications import action_request


async def turn_on(device_id: int):
    message = {"device_id": device_id}
    await action_request("turn_on", message)


async def turn_off(device_id: int):
    message = {"device_id": device_id}
    await action_request("turn_off", message)


async def set_heating_threshold_temperature(device_id: int, value: int):
    message = {"device_id": device_id, "value": value}
    await action_request("set_heating_threshold_temperature", message)


async def set_cooling_threshold_temperature(device_id: int, value: int):
    message = {"device_id": device_id, "value": value}
    await action_request("set_cooling_threshold_temperature", message)


async def set_heater_cooler_mode(device_id: int, mode: str):
    message = {"device_id": device_id, "mode": mode}
    await action_request("set_heater_cooler_mode", message)
