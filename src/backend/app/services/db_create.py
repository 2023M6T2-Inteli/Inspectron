from src.backend.app.config.db_connection import collection_space

post = {"name": "Atelie 01", "coordinates": {"x": 1, "y":2}}

collection_space.insert_one(post)