import os

from pymongo import MongoClient


class MongodbClient:
    def __init__(self, mongo_url):
        self.client = MongoClient(mongo_url)

    def insert(self, chat):
        db = self.client["chatbot"]
        collection = db["chatlog"]          
        collection.insert_one(chat)
