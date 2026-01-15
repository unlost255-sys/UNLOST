import os
from dotenv import load_dotenv
from pymongo import MongoClient
import sys

load_dotenv()

uri = os.getenv('MONGO_URI')
print(f"Loaded URI from env: {uri[:15]}...{uri[-10:] if uri else 'None'}")

if not uri:
    print("Error: MONGO_URI not found.")
    sys.exit(1)

try:
    client = MongoClient(uri)
    # The ismaster command is cheap and does not require auth.
    client.admin.command('ismaster')
    print("Server available.")
    
    # Check auth
    print("Checking auth...")
    db = client.get_database('unlost')
    print(f"Collections: {db.list_collection_names()}")
    print("Auth successful!")
    
except Exception as e:
    print(f"Connection failed: {e}")
