from ..config.db_connection import collection_location

post = {"name": "Atelie 01", "coordinates": {"x": 1, "y":2}}

collection_location.insert_one(post)