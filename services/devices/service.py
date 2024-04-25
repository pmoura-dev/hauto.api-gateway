from typing import List

from models.devices import DeviceDetails


class DeviceService:

    def __init__(self, client):
        self.client = client

    def get_all_device_details(self) -> List[DeviceDetails]:
        return self.client.get_all_device_details()
