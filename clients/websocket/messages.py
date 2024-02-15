import json

from clients.websocket import client


def state_message(device_id: int, state: str):
    message = {"type": state, "device_id": device_id, "state": state}
    client.send_message(json.dumps(message))
