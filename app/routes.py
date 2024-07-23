from .resources.user import UserRegister, UserLogin
# from .resources.quote import QuoteResource, QuoteListResource,QuoteLikeResource
from .resources.quote import (
        QuoteListResource,
        QuoteResource,
        QuoteLikeResource,
        QuoteDislikeResource,
        QuotePageResource,
        RandomQuoteResource,
        CustomNotificationResource,)

def initialize_routes(api):
    api.add_resource(UserRegister, '/register')
    api.add_resource(UserLogin, '/login')

    api.add_resource(QuoteListResource, '/quotes')
    api.add_resource(QuoteResource, '/quotes/<string:quote_id>')
    api.add_resource(QuoteLikeResource, '/quotes/<string:quote_id>/like')
    api.add_resource(QuoteDislikeResource, '/quotes/<string:quote_id>/dislike')
    api.add_resource(QuotePageResource, '/pagequote')
    api.add_resource(RandomQuoteResource, '/getrandomquote')
    api.add_resource(CustomNotificationResource, '/sendcustomnotify')


