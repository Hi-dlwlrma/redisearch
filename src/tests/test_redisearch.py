from src.data.database import Redisearch

if __name__ == "__main__":
    redisearch = Redisearch("idx:test")
    redisearch.retrieve_all_items()
