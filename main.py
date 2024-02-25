from fastapi import FastAPI

from errors.handlers import hauto_error_handler
from errors.models import HAUTOError
from routers.actions import router as actions_router
from routers.devices import router as devices_router

# app = FastAPI(lifespan=streams_router.lifespan_context)
app = FastAPI()
app.include_router(devices_router)
app.include_router(actions_router)
# app.include_router(streams_router)
# app.include_router(websocket_router)

app.add_exception_handler(HAUTOError, hauto_error_handler)
