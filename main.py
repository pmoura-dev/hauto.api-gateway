from fastapi import FastAPI
from faststream.rabbit.fastapi import RabbitRouter

from errors.models import HAUTOError
from errors.handlers import hauto_error_handler
from routers.actions import router as actions_router

router = RabbitRouter("amqp://guest:guest@localhost:5672")


app = FastAPI()
app.include_router(actions_router)

app.add_exception_handler(HAUTOError, hauto_error_handler)

