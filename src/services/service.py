import json

from src.data.database import Redisearch
from src.schemas.schema import Movie


def insert(request: Movie, index_name="idx:test"):
    """Inserts a new request document into the Redisearch index."""
    redisearch = Redisearch(index_name)
    try:
        # Insert the into Redis using hset
        __dict = request.dict()
        __dict["genres"] = json.dumps(__dict["genres"])
        redisearch.client.redis.hset(f"doc:{request.id}", mapping=__dict)
        print(f"Inserted request with ID: {request.id}")
        return redisearch.get_item(request.id)
    except Exception as e:
        print(f"Failed to insert request with ID: {request.id}: {str(e)}")


def delete(request_id: str, index_name="idx:test"):
    """Deletes a request document from the Redisearch index."""
    redisearch = Redisearch(index_name)
    try:
        # Delete the request document from Redisearch
        redisearch.client.delete_document(f"doc:{request_id}")
        print(f"Deleted request with ID: {request_id}")
    except Exception as e:
        print(f"Failed to delete request with ID {request_id}: {str(e)}")


def update(request_id: str, request: Movie, index_name="idx:test"):
    """Updates a request document in the Redisearch index."""
    redisearch = Redisearch(index_name)
    try:
        # Update the request document in Redis using hset
        __dict = request.dict()
        __dict["genres"] = json.dumps(__dict["genres"])
        redisearch.client.redis.hset(f"doc:{request_id}", mapping=__dict)
        print(f"Updated request with ID: {request_id}")
        return redisearch.get_item(request_id)
    except Exception as e:
        print(f"Failed to update request with ID: {request_id}: {str(e)}")


def search(search_term: str, field: str, index_name="idx:test"):
    redisearch = Redisearch(index_name)
    return redisearch.search_document(
        search_term=search_term,
        field=field,
        limit=1000,
        offset=0,
        use_sort_by=True,
        # use_aggregation=True,
    )
