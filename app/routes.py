from .resources.user import UserRegister, UserLogin
from .resources.quote import QuoteResource, QuoteListResource,QuoteLikeResource

def initialize_routes(api):
    api.add_resource(UserRegister, '/register')
    api.add_resource(UserLogin, '/login')
    api.add_resource(QuoteListResource, '/quotes')
    api.add_resource(QuoteResource, '/quotes/<string:quote_id>')
    api.add_resource(QuoteLikeResource, '/quotes/<string:quote_id>/likeordislike')

