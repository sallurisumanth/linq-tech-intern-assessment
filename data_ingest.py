import time, random, os
from datetime import datetime
from pymongo import MongoClient

client = MongoClient(os.getenv("MONGO_URI", "mongodb://localhost:27017"))
coll = client["linq_database"]["category_data"]
cats = ["food", "health", "education", "travel", "entertainment", "shopping"]

try:
    while True:
        coll.insert_many([{"category": c, "value": random.randint(200, 1000), "timestamp": datetime.utcnow()} for c in cats])
        print(f"Inserted {len(cats)} records at {datetime.utcnow()}")
        time.sleep(5)
except KeyboardInterrupt:
    print("Stopped.")
