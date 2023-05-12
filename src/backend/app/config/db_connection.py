import pymongo
from pymongo import MongoClient
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("MONGODB_URI") 

cluster = MongoClient(f"mongodb+srv://gt:{uri}@inspectron.gcegbk5.mongodb.net/?retryWrites=true&w=majority")
db = cluster["Inspectron"]
collection_location = db["location"]
collection_scan = db["scan"]