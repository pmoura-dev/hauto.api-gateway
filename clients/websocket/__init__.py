from starlette.websockets import WebSocket


async def send_message(websocket: WebSocket, message: str):
    await websocket.send_text(message)
