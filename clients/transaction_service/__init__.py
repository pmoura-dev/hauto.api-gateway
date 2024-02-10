import os
from typing import Dict, Any

import requests


class Client:

    def __init__(self, base_url):
        self.base_url = base_url

    def get(self, path: str, params: Dict[str, Any] | None = None) -> requests.Response:
        return requests.get(self.base_url + path, params=params)


client = Client(os.environ.get("transaction_service_host"))
