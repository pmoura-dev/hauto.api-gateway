from pydantic import BaseModel


class HAUTOError(Exception):
    def __init__(self, error: str):
        if error == "":
            error = "Something went wrong."
        self.error = error


class HAUTOErrorResponse(BaseModel):
    error: str
