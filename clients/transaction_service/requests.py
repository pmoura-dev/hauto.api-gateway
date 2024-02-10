from starlette.status import HTTP_404_NOT_FOUND

from clients.transaction_service import client
from clients.transaction_service.types import GetDeviceControlDataResponse


def get_device_control_data(device_id: int) -> GetDeviceControlDataResponse:
    try:
        path = f"/{device_id}/control_data"
        http_response = client.get(path)

        if http_response.status_code == HTTP_404_NOT_FOUND:
            raise Exception

        http_response = http_response.json()
        return GetDeviceControlDataResponse(
            natural_id=http_response["natural_id"],
            controller=http_response["controller"]
        )
    except Exception:
        raise
