from typing import Protocol, Optional
from uuid import uuid4, UUID

from pydantic import BaseModel, Field


class Metadata(BaseModel):
    correlation_id: UUID = Field(default_factory=uuid4)


class Message(BaseModel):
    meta: Metadata


class Publisher(Protocol):
    async def publish(self, topic: str, message: Message, extras: Optional[dict]) -> None:
        pass
