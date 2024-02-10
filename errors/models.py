from pydantic import BaseModel


class HAUTOError(Exception):

    def __init__(self, code: int, message: str):
        self.code = code
        self.message = message


class HAUTOErrorResponse(BaseModel):
    code: int
    message: str
