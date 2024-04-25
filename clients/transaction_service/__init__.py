from typing import Dict, Any, List

import requests

import config
from models.devices import DeviceDetails


class Client:

    def __init__(self):
        self.url = f"http://{config.TRANSACTION_SERVICE_HOST}:{config.TRANSACTION_SERVICE_PORT}"

    def execute(self, proc_name: str, params: Dict[str, Any]) -> Any:
        response = requests.post(f"{self.url}/execute/{proc_name}", json=params)

        data = response.json()
        return data

    def get_all_device_details(self) -> List[DeviceDetails]:
        proc_name = "devices/get_all_device_details"

        data = self.execute(proc_name, {})
        return [DeviceDetails.parse_obj(d) for d in data]
