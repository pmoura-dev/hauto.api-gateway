import requests
from fastapi.encoders import jsonable_encoder
from faststream.rabbit import ExchangeType, RabbitExchange, RabbitQueue
from faststream.rabbit.fastapi import RabbitRouter

import config
from rabbitmq.types import *
from services.notifications import notification_service

router = RabbitRouter(
    host=config.RABBITMQ_HOST,
    port=config.RABBITMQ_PORT,
    login=config.RABBITMQ_USER,
    password=config.RABBITMQ_PASSWORD,
)

devices_exchange = RabbitExchange(DEVICES_EXCHANGE, durable=True, type=ExchangeType.TOPIC)

action_successes_queue = RabbitQueue(ACTION_SUCCESSES_QUEUE, auto_delete=True,
                                     routing_key=ACTION_SUCCEEDED_TOPIC)
action_failures_queue = RabbitQueue(ACTION_FAILURES_QUEUE, auto_delete=True,
                                    routing_key=ACTION_FAILED_TOPIC)
state_updates_queue = RabbitQueue(STATE_UPDATES_QUEUE, auto_delete=True,
                                  routing_key=STATE_UPDATED_TOPIC)


@router.subscriber(action_successes_queue, devices_exchange)
async def handle_action_success(correlation_id: CorrelationID, message: ActionSucceededMessage):
    if message.callback_url is None:
        return

    requests.post(message.callback_url, json={
        "correlation_id": correlation_id,
        "success": True
    })


@router.subscriber(action_failures_queue, devices_exchange)
async def handle_action_failure(correlation_id: CorrelationID, message: ActionFailedMessage):
    if message.callback_url is None:
        return

    requests.post(message.callback_url, json={
        "correlation_id": correlation_id,
        "success": False,
        "error": message.error
    })


@router.subscriber(state_updates_queue, devices_exchange)
async def handle_state_updates(message: StateUpdatedMessage):
    notification_service.send_notification(jsonable_encoder(message, exclude_none=True))