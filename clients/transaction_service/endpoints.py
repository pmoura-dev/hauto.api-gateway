from clients.transaction_service import client


def get_device(device_id: int) -> dict:
    path = f"/execute/get_device"
    return client.post(path, body={"device_id": device_id})


def get_device_state(device_id: int) -> dict:
    path = f"/execute/get_device_state"
    return client.post(path, body={"device_id": device_id})
