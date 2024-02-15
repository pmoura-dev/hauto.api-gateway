from fastapi import FastAPI

from errors.handlers import hauto_error_handler
from errors.models import HAUTOError
from routers.actions import router as actions_router
from routers.streams import router as streams_router
from routers.websocket import router as websocket_router

app = FastAPI(lifespan=streams_router.lifespan_context)
app.include_router(actions_router)
app.include_router(streams_router)
app.include_router(websocket_router)

app.add_exception_handler(HAUTOError, hauto_error_handler)
