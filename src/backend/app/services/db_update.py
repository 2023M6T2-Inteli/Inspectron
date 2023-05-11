from src.backend.app.config.db_connection import collection_space

collection_space.update_one({"name": "Atelie 01"}, {"$set":{"name": "Atelie 93"}})