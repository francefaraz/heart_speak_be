from app.extensions import mongo

class User:
    @staticmethod
    def find_by_email(email):
        return mongo.db.RegisteredUsers.find_one({"email": email})

    @staticmethod
    def find_by_username(username):
        return mongo.db.RegisteredUsers.find_one({"username": username})

    @staticmethod
    def insert(user_data):
        return mongo.db.RegisteredUsers.insert_one(user_data)
