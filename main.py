from typing import List

from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pymongo import MongoClient

# FastAPI setup
app = FastAPI()

# Serve static frontend
app.mount("/static", StaticFiles(directory="static"), name="static")

# MongoDB connection
client = MongoClient("mongodb://localhost:27017/")
db = client.board_app
positions = db.positions

# Init square if not exists
if not positions.find_one({"id": 1}):
    positions.insert_one({"id": 1, "row": 0, "col": 0})

# Active WebSocket clients
clients: List[WebSocket] = []


@app.get("/")
async def root():
    return HTMLResponse('<script>window.location="/static/index.html"</script>')


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)

    # Send current square position
    pos = positions.find_one({"id": 1}, {"_id": 0})
    await websocket.send_json(pos)

    try:
        while True:
            data = await websocket.receive_json()
            positions.update_one({"id": 1}, {"$set": data})
            for client in clients:
                if client != websocket:
                    await client.send_json(data)
    except WebSocketDisconnect:
        clients.remove(websocket)
