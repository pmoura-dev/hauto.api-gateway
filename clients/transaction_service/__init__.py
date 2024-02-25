import json
from typing import Dict, Any

import requests
from starlette import status

import config


class RecordNotFoundException(Exception):
    pass


class Client:

    def __init__(self, host, port):
        self.base_url = f"http://{host}:{port}"

    def post(self, path: str, body: Dict[str, Any] | None = None) -> Any:
        response = requests.post(self.base_url + path, data=json.dumps(body).encode('utf-8'))
        if response.status_code == status.HTTP_404_NOT_FOUND:
            raise RecordNotFoundException
        return response.json()

    def execute(self, proc_name: str, params: Dict[str, Any] | None = None) -> Any:
        data = {"proc_name": proc_name}
        if params is not None:
            data["params"] = params

        response = requests.post(self.base_url + "/execute", data=data)
        if response.status_code == status.HTTP_404_NOT_FOUND:
            raise RecordNotFoundException

        return response.json()

    def get(self, path: str, params: Dict[str, Any] | None = None) -> requests.Response:
        print(self.base_url + path)
        return requests.get(self.base_url + path, params=params)


client = Client(
    host=config.TRANSACTION_SERVICE_HOST,
    port=config.TRANSACTION_SERVICE_PORT
)
