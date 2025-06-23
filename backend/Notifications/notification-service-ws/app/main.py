
from fastapi import FastAPI, WebSocket
from app.routes import notify
from app.services.manager import connection_manager

app = FastAPI()

app.include_router(notify.router, prefix="/notify", tags=["Notifications"])

@app.websocket("/ws/notify")
async def websocket_endpoint(websocket: WebSocket):
    await connection_manager.connect(websocket)
    try:
        while True:
            await websocket.receive_text()  # keep connection alive
    except Exception:
        pass
    finally:
        await connection_manager.disconnect(websocket)
