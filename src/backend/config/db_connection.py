import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("MONGODB_URI") 

cluster = MongoClient(uri)
db = cluster["Inspectron"]
collection_location = db["location"]
collection_scan = db["scan"]