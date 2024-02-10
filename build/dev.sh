#!/bin/bash

# Hosts
env rabbitmq_host="amqp://guest:guest@localhost:5672"
env transaction_service_host="localhost:8081"

uvicorn main:app --reload