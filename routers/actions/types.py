from uuid import UUID

from fastapi import Query
from pydantic import BaseModel

# query params
callback_url_param = Query(
    default=None,
    title="Callback URL",
    description="URL that will be called by HAUTO as soon as the operation is completed."
)


# responses
class ActionAcceptedResponse(BaseModel):
    correlation_id: UUID
