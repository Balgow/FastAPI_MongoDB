from pymongo import MongoClient

DATABASE_URL = 'mongodb+srv://admin:admin@testcluster0.fgc6lja.mongodb.net/?retryWrites=true&w=majority'    
client = MongoClient(DATABASE_URL)
db = client.test
collection_name = db['testcollection0']
