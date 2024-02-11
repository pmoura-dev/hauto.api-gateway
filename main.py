from fastapi import FastAPI

from errors.models import HAUTOError
from errors.handlers import hauto_error_handler
from routers.actions import router as actions_router

app = FastAPI()
app.include_router(actions_router)

app.add_exception_handler(HAUTOError, hauto_error_handler)
