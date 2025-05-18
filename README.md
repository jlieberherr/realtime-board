# 🧩 Real-Time Drag-and-Drop Grid with FastAPI & WebSockets

A simple real-time 6x6 board where a square can be dragged and dropped between cells. The square's position is synchronized across all clients using WebSockets and stored in MongoDB.

---

## 🚀 Features

- ✅ Drag-and-drop UI (6x6 grid)
- ✅ Real-time sync with WebSockets
- ✅ FastAPI backend
- ✅ MongoDB persistence
- ✅ Pure HTML/CSS/JavaScript frontend

---

## 📦 Requirements

- Python 3.9+
- MongoDB (running locally)
- pip (Python package installer)

---

## 🛠️ Installation

### 1. Clone the repository

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
```

### 2. Create and activate a virtual environment
```bash
python -m venv venv
# Windows:
venv\Scripts\activate
# macOS/Linux:
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. MongoDB Setup
```bash
net start MongoDB  # Windows service
# OR:
"C:\Program Files\MongoDB\Server\6.0\bin\mongod.exe" --dbpath="C:\data\db"
```

### 5. Initialize Database
```bash
python init_db.py
```

---

## ▶️ Run the App
```bash
uvicorn main:app --reload
```
Open your browser and go to:
```bash
http://127.0.0.1:8000
```
✅ Try opening it in two tabs — move the red square in one, and see it update in the other!
