from pymongo import MongoClient

client = MongoClient()
db = client['tweets']
db['elonmusk'].create_index([('Tweet_Id', pymongo.ASCENDING)], unique=True)