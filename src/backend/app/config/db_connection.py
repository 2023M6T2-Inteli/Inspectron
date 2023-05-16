from mongoengine import *
from dotenv import load_dotenv
import os

load_dotenv()

uri = os.getenv("MONGODB_URI") 

connect(host=uri)
