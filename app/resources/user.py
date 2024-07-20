from flask_restful import Resource, reqparse
from injector import inject
from app.services.user_service import UserService

class UserRegister(Resource):
    @inject
    def __init__(self, user_service: UserService):
        self.user_service = user_service
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('email', type=str, required=True, help='Email cannot be blank')
        self.parser.add_argument('username', type=str, required=True, help='Username cannot be blank')
        self.parser.add_argument('password', type=str, required=True, help='Password cannot be blank')

    def post(self):
        data = self.parser.parse_args()
        return self.user_service.register(data)

class UserLogin(Resource):
    @inject
    def __init__(self, user_service: UserService):
        self.user_service = user_service
        self.parser = reqparse.RequestParser()
        self.parser.add_argument('username', type=str, required=True, help='Username cannot be blank')
        self.parser.add_argument('password', type=str, required=True, help='Password cannot be blank')

    def post(self):
        data = self.parser.parse_args()
        return self.user_service.login(data)
