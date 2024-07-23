from flask_restful import Resource, reqparse
from flask import request
from injector import inject
from app.services.quote_service import QuoteService

class QuoteListResource(Resource):
    @inject
    def __init__(self, quote_service: QuoteService):
        self.quote_service = quote_service

    def get(self):
        return self.quote_service.get_all_quotes()

    def post(self):
        parser = reqparse.RequestParser()
        parser.add_argument('quote', type=str, required=True, help='Quote cannot be blank')
        parser.add_argument('quoteTitle', type=str, required=True, help='Quote title cannot be blank')
        parser.add_argument('quoteAuthor', type=str, required=False, help='Quote author cannot be blank')
        parser.add_argument('likes', type=int, required=False)
        parser.add_argument('dislikes', type=int, required=False)
        data = parser.parse_args()
        return self.quote_service.create_quote(data), 201

class QuoteResource(Resource):
    @inject
    def __init__(self, quote_service: QuoteService):
        self.quote_service = quote_service

    def get(self, quote_id):
        return self.quote_service.get_quote(quote_id)

class QuoteLikeResource(Resource):
    @inject
    def __init__(self, quote_service: QuoteService):
        self.quote_service = quote_service

    def put(self, quote_id):
        data = request.get_json()
        increment = data.get('increment', True)
        return self.quote_service.update_likes(quote_id, increment)

class QuoteDislikeResource(Resource):
    @inject
    def __init__(self, quote_service: QuoteService):
        self.quote_service = quote_service

    def put(self, quote_id):
        data = request.get_json()
        increment = data.get('increment', True)
        return self.quote_service.update_dislikes(quote_id, increment)

class QuotePageResource(Resource):
    @inject
    def __init__(self, quote_service: QuoteService):
        self.quote_service = quote_service

    def get(self):
        parser = reqparse.RequestParser()
        parser.add_argument('page', type=int, required=True, help='Page number is required')
        parser.add_argument('per_page', type=int, required=True, help='Per page count is required')
        args = parser.parse_args()
        return self.quote_service.get_page_quote(args['page'], args['per_page'])

class RandomQuoteResource(Resource):
    @inject
    def __init__(self, quote_service: QuoteService):
        self.quote_service = quote_service

    def get(self):
        return self.quote_service.get_random_quote()

class CustomNotificationResource(Resource):
    @inject
    def __init__(self, quote_service: QuoteService):
        self.quote_service = quote_service

    def post(self):
        data = request.get_json()
        return self.quote_service.send_custom_notification(data)
