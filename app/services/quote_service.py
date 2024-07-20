from app.models.quote import Quote

class QuoteService:
    def get_all_quotes(self):
        return Quote.find_all()

    def get_quote(self, quote_id):
        quote = Quote.find_by_id(quote_id)
        if quote:
            return quote
        return {'message': 'Quote not found'}, 404

    def create_quote(self, data):
        quote_data = {
            'quote': data['quote'],
            'quoteTitle': data['quoteTitle'],
            'quoteAuthor': data.get('quoteAuthor', "Shaik Muneer"),
            'likes': data.get('likes', 0),
            'dislikes': data.get('dislikes', 0)
        }
        Quote.insert(quote_data)
        return quote_data

    def update_quote(self, quote_id, data):
        quote = Quote.find_by_id(quote_id)
        if quote:
            Quote.update(quote_id, data)
            return data
        return {'message': 'Quote not found'}, 404

    def delete_quote(self, quote_id):
        if Quote.delete(quote_id):
            return {'message': 'Quote deleted'}, 200
        return {'message': 'Quote not found'}, 404
    
    def update_likes(self, quote_id, increment=True):
        result = Quote.update_like_or_dislike(quote_id, increment)
        if result.matched_count:
            return {'message': 'Quote likes updated'}, 200
        return {'message': 'Quote not found'}, 404