import os
from typing import Dict, Any

import requests

import config


class Client:

    def __init__(self, host, port):
        self.base_url = f"http://{host}:{port}"

    def get(self, path: str, params: Dict[str, Any] | None = None) -> requests.Response:
        return requests.get(self.base_url + path, params=params)


client = Client(
    host=config.TRANSACTION_SERVICE_HOST,
    port=config.TRANSACTION_SERVICE_PORT
)
