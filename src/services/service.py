from src.data.database import Redisearch
from src.schemas.schema import Request


def insert(request: Request, index_name="idx:test"):
    """Inserts a new request document into the Redisearch index."""
    redisearch = Redisearch(index_name)
    try:
        # Insert the into Redis using hset
        redisearch.client.redis.hset(f"doc:{request.id}", mapping=request.dict())
        print(f"Inserted request with ID: {request.id}")
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


def update(request_id: str, request: Request, index_name="idx:test"):
    """Updates a request document in the Redisearch index."""
    redisearch = Redisearch(index_name)
    try:
        # Update the request document in Redis using hset
        redisearch.client.redis.hset(
            f"doc:{request_id}", mapping={"name": request.name}
        )
        print(f"Updated request with ID: {request_id}")
    except Exception as e:
        print(f"Failed to update request with ID: {request_id}: {str(e)}")
