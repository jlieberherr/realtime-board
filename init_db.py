from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client.board_app
positions = db.positions

positions.delete_many({"id": 1})
positions.insert_one({"id": 1, "row": 0, "col": 0})

print("✅ MongoDB initialized with default square position.")
