import os

APP_HOST = os.getenv("APP_HOST", "localhost")

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "localhost")
RABBITMQ_PORT = os.getenv("RABBITMQ_PORT", "5672")
RABBITMQ_USER = os.getenv("RABBITMQ_USER", "guest")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD", "guest")

TRANSACTION_SERVICE_HOST = os.getenv("TRANSACTION_SERVICE_HOST", "localhost")
TRANSACTION_SERVICE_PORT = os.getenv("TRANSACTION_SERVICE_PORT", "8080")
