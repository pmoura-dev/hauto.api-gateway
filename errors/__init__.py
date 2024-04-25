from pydantic import BaseModel


class HAUTOAPIError(Exception):
    def __init__(self, error: str = "Something went wrong"):
        self.error = error


class HAUTOAPIErrorResponse(BaseModel):
    error: str
