from app import app, mongo, bcrypt
from datetime import datetime, timezone

def create_admin():
    with app.app_context():
        email = 'admin@unlost.com'
        password = 'admin123'
        username = 'admin'
        
        # Check if user exists
        existing_user = mongo.db.users.find_one({"email": email})
        
        if existing_user:
            print(f"User with email {email} already exists.")
            if existing_user.get('is_admin'):
                print("User is already an admin.")
            else:
                mongo.db.users.update_one(
                    {"email": email},
                    {"$set": {"is_admin": True}}
                )
                print(f"User {email} promoted to admin.")
        else:
            hashed_password = bcrypt.generate_password_hash(password).decode('utf-8')
            new_user = {
                "username": username,
                "email": email,
                "password": hashed_password,
                "is_admin": True,
                "date_created": datetime.now(timezone.utc)
            }
            mongo.db.users.insert_one(new_user)
            print(f"Admin user created:\nEmail: {email}\nPassword: {password}")

if __name__ == '__main__':
    create_admin()
