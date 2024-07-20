from bson import ObjectId
from flask import jsonify
from app.extensions import mongo

def convert_to_serializable(doc):
    """
    Convert MongoDB document to a JSON-serializable dictionary.
    """
    doc['_id'] = str(doc['_id'])
    return doc

class Quote:
    @staticmethod
    def find_all():
        # quotes = list(mongo.db.quotes.find({}))
        # for quote in quotes:
        #     quote['_id'] = str(quote['_id'])  # Convert ObjectId to string
        # return jsonify({'quotes': quotes})
        quotes = list(mongo.db.quotes.find())
        return [convert_to_serializable(quote) for quote in quotes]
        # print("here",mongo.db.quotes.find())
        # for quote in list(mongo.db.quotes.find()):
        #     quote['_id'] = str(quote['_id'])  # Convert ObjectId to string
        # return jsonify({'quotes': quotes})
        # return list(mongo.db.quotes.find())

    @staticmethod
    def find_by_id(quote_id):
        quote = mongo.db.Quotes.find_one({"_id": ObjectId(quote_id)})
        return convert_to_serializable(quote) if quote else None

    @staticmethod
    def insert(quote_data):
        return mongo.db.Quotes.insert_one(quote_data)

    @staticmethod
    def update(quote_id, quote_data):
        return mongo.db.Quotes.update_one({"_id": quote_id}, {"$set": quote_data})

    @staticmethod
    def delete(quote_id):
        return mongo.db.Quotes.delete_one({"_id": quote_id})

    @staticmethod
    def update_like_or_dislike(quote_id, increment=True):
        update = {"$inc": {"likes": 1}} if increment else {"$inc": {"likes": -1}}
        return mongo.db.quotes.update_one({"_id": ObjectId(quote_id)}, update)