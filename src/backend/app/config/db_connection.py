import pymongo
from pymongo import MongoClient

cluster = MongoClient("mongodb+srv://gustavo-francisco:M1e2c3a4d@inspectron.9igr5b1.mongodb.net/?retryWrites=true&w=majority")
db = cluster["Inspectron"]
collection_space = db["space"]
collection_route = db["route"]