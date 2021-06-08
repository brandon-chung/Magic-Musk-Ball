from pymongo import MongoClient
import pymongo

client = MongoClient()
db = client["tweets"]
db["elonmusk"].create_index([("Tweet_Id", pymongo.ASCENDING)], unique=True)
