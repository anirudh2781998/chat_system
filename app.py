from fastapi import FastAPI, WebSocket
import sqlite3

app = FastAPI()
clients = []

# DB setup
conn = sqlite3.connect("chat.db", check_same_thread=False)
cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS messages (msg TEXT)")
conn.commit()

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    clients.append(websocket)

    try:
        while True:
            data = await websocket.receive_text()

            # store message
            cursor.execute("INSERT INTO messages VALUES (?)", (data,))
            conn.commit()

            # broadcast
            for client in clients:
                await client.send_text(data)

    except:
        clients.remove(websocket)