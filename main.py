from flask import Flask
from flask_restful import Api
from flask_injector import FlaskInjector
from injector import Binder, singleton
from app.config import Config
from app.extensions import mongo
from app.routes import initialize_routes
from app.services.user_service import UserService
from app.services.email_service import EmailService
from app.services.push_service import PushService
from app.services.quote_service import QuoteService
import sys
import os

sys.path.append(os.path.dirname(os.path.abspath(__file__)))

def configure(binder: Binder):
    binder.bind(UserService, to=UserService, scope=singleton)
    binder.bind(EmailService, to=EmailService, scope=singleton)
    binder.bind(PushService, to=PushService, scope=singleton)
    binder.bind(QuoteService, to=QuoteService, scope=singleton)

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    mongo.init_app(app)

    api = Api(app)
    initialize_routes(api)

    FlaskInjector(app=app, modules=[configure])

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True)
