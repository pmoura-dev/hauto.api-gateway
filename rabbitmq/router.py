import requests
from fastapi.encoders import jsonable_encoder
from faststream.rabbit import ExchangeType, RabbitExchange, RabbitQueue
from faststream.rabbit.fastapi import RabbitRouter

import config
from rabbitmq.types import DEVICES_EXCHANGE, ACTION_SUCCESSES_QUEUE, ACTION_SUCCEEDED_TOPIC, ACTION_FAILURES_QUEUE, \
    ACTION_FAILED_TOPIC, STATE_UPDATES_QUEUE, STATE_UPDATED_TOPIC, CorrelationID, ActionSucceededMessage, \
    ActionFailedMessage, StateUpdatedMessage
from services.notifications import notification_service
from services.notifications.service import NotificationMessage, NotificationType

router = RabbitRouter(
    host=config.RABBITMQ_HOST,
    port=int(config.RABBITMQ_PORT),
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
    notification = NotificationMessage(
        type=NotificationType.STATE,
        message=message
    )

    notification_service.send_notification(jsonable_encoder(notification, exclude_none=True))
