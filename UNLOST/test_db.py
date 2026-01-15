import os
import certifi
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

uri = os.getenv('MONGO_URI')
print(f"Testing connection to: {uri.split('@')[1] if '@' in uri else 'LOCAL/UNKNOWN'}")

try:
    print(f"Attempting connection to local MongoDB...")
    client = MongoClient("mongodb://localhost:27017/", serverSelectionTimeoutMS=5000)
    print("Client initialized. Checking server status...")
    info = client.admin.command('ismaster')
    print("Connection Successful!")
    print(f"Server version: {info.get('version')}")
except Exception as e:
    print(f"Connection Failed: {e}")
    import traceback
    traceback.print_exc()
