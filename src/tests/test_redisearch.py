from src.data.database import Redisearch

if __name__ == "__main__":
    redisearch = Redisearch("idx:test")
    redisearch.get_index()
    # print(redisearch.get_item(1))
    # res = redisearch.search_document(
    #     search_term="Gore",
    #     field="director",
    #     limit=10,
    #     offset=0,
    #     # use_aggregation=True,
    #     use_scorer=True,
    #     # use_sort_by=True,
    # )
    # print(res)
