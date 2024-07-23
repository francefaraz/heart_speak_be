from bson import ObjectId
from flask import jsonify
from app.extensions import mongo
import random
from pymongo import MongoClient


from bson import ObjectId
from pymongo import MongoClient
import random

class Quote:
    @staticmethod
    def to_json(quote):
        print(quote)
        return {
            "_id": str(quote["_id"]),
            "quote": quote["quote"],
            "quoteTitle": quote.get("quoteTitle","Today's Quote"),
            "quoteAuthor": quote.get("quoteAuthor", "Shaik Muneer"),
            "likes": quote.get("likes", 0),
            "dislikes": quote.get("dislikes", 0)
        }

    @staticmethod
    def find_all():
        return [Quote.to_json(quote) for quote in mongo.db.quotes.find()]

    @staticmethod
    def find_with_pagination(skip, limit):
        return [Quote.to_json(quote) for quote in mongo.db.quotes.find().skip(skip).limit(limit)]

    @staticmethod
    def find_random():
        count = mongo.db.quotes.count_documents({})
        if count == 0:
            return None
        random_index = random.randint(0, count - 1)
        return Quote.to_json(list(mongo.db.quotes.find().limit(1).skip(random_index))[0])

    @staticmethod
    def find_by_id(quote_id):
        quote = mongo.db.quotes.find_one({"_id": ObjectId(quote_id)})
        if quote:
            return Quote.to_json(quote)
        return None

    @staticmethod
    def insert(quote_data):
        return mongo.db.quotes.insert_one(quote_data)

    @staticmethod
    def update(quote_id, quote_data):
        return mongo.db.quotes.update_one({"_id": ObjectId(quote_id)}, {"$set": quote_data})

    @staticmethod
    def update_likes(quote_id, increment=True):
        update = {"$inc": {"likes": 1}} if increment else {"$inc": {"likes": -1}}
        return mongo.db.quotes.update_one({"_id": ObjectId(quote_id)}, update)

    @staticmethod
    def update_dislikes(quote_id, increment=True):
        update = {"$inc": {"dislikes": 1}} if increment else {"$inc": {"dislikes": -1}}
        return mongo.db.quotes.update_one({"_id": ObjectId(quote_id)}, update)

    @staticmethod
    def delete(quote_id):
        return mongo.db.quotes.delete_one({"_id": ObjectId(quote_id)})

def convert_to_serializable(doc):
    """
    Convert MongoDB document to a JSON-serializable dictionary.
    """
    doc['_id'] = str(doc['_id'])
    return doc

# class Quote:
    
#     # @staticmethod
#     # def find_all():
#     #     # quotes = list(mongo.db.quotes.find({}))
#     #     # for quote in quotes:
#     #     #     quote['_id'] = str(quote['_id'])  # Convert ObjectId to string
        # return jsonify({'quotes': quotes})
        # quotes = list(mongo.db.quotes.find())
        # return [convert_to_serializable(quote) for quote in quotes]
        # print("here",mongo.db.quotes.find())
        # for quote in list(mongo.db.quotes.find()):
        #     quote['_id'] = str(quote['_id'])  # Convert ObjectId to string
    # #     # return jsonify({'quotes': quotes})
    # #     # return list(mongo.db.quotes.find())

    # @staticmethod
    # def find_all():
    #     return list(mongo.db.quotes.find())

    # @staticmethod
    # def find_with_pagination(skip, limit):
    #     return list(mongo.db.quotes.find().skip(skip).limit(limit))

    # @staticmethod
    # def find_random():
    #     count = mongo.db.quotes.count_documents({})
    #     if count == 0:
    #         return None
    #     random_index = random.randint(0, count - 1)
    #     return list(mongo.db.quotes.find().limit(1).skip(random_index))[0]

    # @staticmethod
    # def find_by_id(quote_id):
    #     return mongo.db.quotes.find_one({"_id": quote_id})

    # @staticmethod
    # def insert(quote_data):
    #     return mongo.db.quotes.insert_one(quote_data)

    # @staticmethod
    # def update(quote_id, quote_data):
    #     return mongo.db.quotes.update_one({"_id": quote_id}, {"$set": quote_data})

    # @staticmethod
    # def update_likes(quote_id, increment=True):
    #     update = {"$inc": {"likes": 1}} if increment else {"$inc": {"likes": -1}}
    #     return mongo.db.quotes.update_one({"_id": quote_id}, update)

    # @staticmethod
    # def update_dislikes(quote_id, increment=True):
    #     update = {"$inc": {"dislikes": 1}} if increment else {"$inc": {"dislikes": -1}}
    #     return mongo.db.quotes.update_one({"_id": quote_id}, update)

    # @staticmethod
    # def delete(quote_id):
    #     return mongo.db.quotes.delete_one({"_id": quote_id})
