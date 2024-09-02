from src.core.database import Redisearch

if __name__ == "__main__":
    redisearch = Redisearch("idx:test")
    redisearch.get_index()
