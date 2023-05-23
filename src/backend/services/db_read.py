from src.backend.app.config.db_connection import collection_space

results = collection_space.find({"name": "Atelie 93"})

for result in results:
    print(result)
