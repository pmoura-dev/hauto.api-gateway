from pydantic import BaseModel


class GetDeviceControlDataResponse(BaseModel):
    natural_id: str
    controller: str
