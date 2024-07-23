from app.models.quote import Quote

class QuoteService:
    def get_all_quotes(self):
        return Quote.find_all()

    def get_page_quote(self, page, per_page):
        skip = (page - 1) * per_page
        return Quote.find_with_pagination(skip, per_page)

    def get_random_quote(self):
        quote = Quote.find_random()
        if quote:
            return quote
        return {'message': 'No quotes available'}, 404

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

    def update_likes(self, quote_id, increment=True):
        result = Quote.update_likes(quote_id, increment)
        if result.matched_count:
            return {'message': 'Quote likes updated'}, 200
        return {'message': 'Quote not found'}, 404

    def update_dislikes(self, quote_id, increment=True):
        result = Quote.update_dislikes(quote_id, increment)
        if result.matched_count:
            return {'message': 'Quote dislikes updated'}, 200
        return {'message': 'Quote not found'}, 404

    def delete_quote(self, quote_id):
        if Quote.delete(quote_id):
            return {'message': 'Quote deleted'}, 200
        return {'message': 'Quote not found'}, 404

    def send_custom_notification(self, data):
        # Implement your notification logic here
        pass
