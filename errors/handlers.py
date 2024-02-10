from fastapi.encoders import jsonable_encoder
from fastapi.requests import Request
from fastapi.responses import JSONResponse

from errors.models import HAUTOError, HAUTOErrorResponse


async def hauto_error_handler(_: Request, error: HAUTOError):
    return JSONResponse(
        status_code=error.code,
        content={"error": jsonable_encoder(HAUTOErrorResponse(code=error.code, message=error.message)) }
    )
