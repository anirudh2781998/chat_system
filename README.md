# 💬 Real-Time Chat System — WebSocket-Based Messaging Service

A lightweight real-time chat application built using FastAPI and WebSockets, designed to handle concurrent client connections with low-latency message delivery.

---

## 🚀 Features

* 🔹 Real-time bidirectional communication using WebSockets
* 🔹 Supports multiple concurrent users
* 🔹 Broadcast messaging to all connected clients
* 🔹 Persistent message storage using SQLite
* 🔹 Asynchronous handling for efficient concurrency
* 🔹 Lightweight and easy to deploy

---

## 🏗️ Tech Stack

* **Backend:** Python (FastAPI)
* **Protocol:** WebSockets
* **Database:** SQLite3
* **Server:** Uvicorn

---

## 🧠 System Design Overview

* Clients connect via WebSocket (`/ws` endpoint)
* Messages are received asynchronously from clients
* Each message is:

  * Stored in SQLite for persistence
  * Broadcasted to all active connections
* FastAPI’s async event loop ensures efficient handling of concurrent users

---

## 📡 WebSocket Endpoint

### 🔹 Connect

```
ws://localhost:8000/ws
```

### 🔹 Message Format (example)

```json
{
  "user": "Anirudh",
  "msg": "Hello world"
}
```

---

## ⚡ Performance

* Handles multiple concurrent WebSocket connections
* Low-latency message delivery (real-time)
* Efficient async architecture using event loop
* Tested locally with multiple simultaneous clients

---

## ▶️ Running Locally

### 1. Clone the repository

```bash
git clone https://github.com/anirudh2781998/chat-system.git
cd chat-system
```

### 2. Install dependencies

```bash
pip install fastapi uvicorn
```

### 3. Run the server

```bash
uvicorn app:app --reload
```

Server will start at:

```
http://localhost:8000
```

---

## 🧪 Testing the Chat System

Use any WebSocket client like:

* https://www.piesocket.com/websocket-tester

Connect to:

```
ws://localhost:8000/ws
```

Open multiple tabs to simulate multiple users and test real-time messaging.

---

## 📂 Project Structure

```
chat-system/
│── app.py
│── chat.db
│── requirements.txt
│── README.md
```

---

## 🔒 Future Improvements

* User authentication & session handling
* Private messaging / chat rooms
* Redis Pub/Sub for horizontal scaling
* Message queue integration (Kafka / RabbitMQ)
* Frontend UI (React / Web client)
* Deployment using Docker & AWS

---

## 👨‍💻 Author

**Anirudh Pandey**

* GitHub: https://github.com/anirudh2781998
* Email: [pandeyanirudh92@gmail.com](mailto:pandeyanirudh92@gmail.com)

---

## ⭐ Show Your Support

If you found this project useful, consider giving it a ⭐ on GitHub!
