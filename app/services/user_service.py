from app.models.user import User
from werkzeug.security import generate_password_hash, check_password_hash

class UserService:
    def register(self, data):
        if User.find_by_email(data['email']) or User.find_by_username(data['username']):
            return {'message': 'User already exists'}, 400

        hashed_password = generate_password_hash(data['password'], method='sha256')
        user_data = {
            'email': data['email'],
            'username': data['username'],
            'password': hashed_password
        }
        User.insert(user_data)
        return {'message': 'User created successfully'}, 201

    def login(self, data):
        user = User.find_by_username(data['username'])
        if user and check_password_hash(user['password'], data['password']):
            return {'message': 'Logged in successfully'}, 200
        return {'message': 'Invalid credentials'}, 401
