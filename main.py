from fastapi import FastAPI, Request
from fastapi.encoders import jsonable_encoder
from starlette.responses import JSONResponse

from docs import tags_metadata
from errors import HAUTOAPIError, HAUTOAPIErrorResponse
from rabbitmq.router import router as rabbitmq_router
from routers.actions.routes import router as actions_router
from routers.devices.routes import router as devices_router
from routers.notifications.routes import router as notifications_router

app = FastAPI(openapi_tags=tags_metadata, lifespan=rabbitmq_router.lifespan_context)
app.include_router(actions_router)
app.include_router(devices_router)
app.include_router(notifications_router)
app.include_router(rabbitmq_router)


@app.exception_handler(HAUTOAPIError)
async def hauto_error_handler(_: Request, exc: HAUTOAPIError):
    return JSONResponse(status_code=500, content=jsonable_encoder(HAUTOAPIErrorResponse(error=exc.error)))
