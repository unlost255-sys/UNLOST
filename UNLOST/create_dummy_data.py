from app import app, mongo
from datetime import datetime, timedelta, timezone

def create_dummy_data():
    with app.app_context():
        # Check if items already exist
        if mongo.db.items.count_documents({}) > 0:
            print("Database already contains data.")
            return

        # Current time as base
        now = datetime.now(timezone.utc)
        # Normalize to midnight for simpler date comparison if desired, 
        # OR keep time. sticking to previous behavior approx.
        # But for date filter to work nicely with range, we better have datetimes.
        
        items = [
            {
                "title": "Black Leather Wallet",
                "description": "Lost my black leather wallet near the cafeteria. It has my ID and some cash.",
                "category": "Accessories",
                "location": "Cafeteria",
                "status": "Lost",
                "contact_info": "student1@campus.edu",
                "date": now
            },
            {
                "title": "Calculus Textbook",
                "description": "Found a Calculus II textbook left on a bench in the quad.",
                "category": "Books",
                "location": "Main Quad",
                "status": "Found",
                "contact_info": "finder@campus.edu",
                "date": now - timedelta(days=1)
            },
            {
                "title": "AirPods Pro Case",
                "description": "Found a white charging case for AirPods Pro.",
                "category": "Electronics",
                "location": "Library 3rd Floor",
                "status": "Found",
                "contact_info": "library_lost_found@campus.edu",
                "date": now - timedelta(days=2)
            },
            {
                "title": "Blue Water Bottle",
                "description": "Lost a blue hydroflask with stickers on it.",
                "category": "Other",
                "location": "Gym",
                "status": "Lost",
                "contact_info": "athlete@campus.edu",
                "date": now - timedelta(days=3)
            }
        ]

        mongo.db.items.insert_many(items)
        print("Dummy data added successfully!")

if __name__ == '__main__':
    create_dummy_data()
