from redis import Redis, ResponseError
from redisearch import Client, IndexDefinition, TextField

from src.config import REDIS_HOST, REDIS_PORT


class Redisearch:
    def __init__(self, index_name=None):
        self.index_name = index_name
        self.redis_conn = Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
        self.client = Client(self.index_name)

    def create_index(self):
        """Creates an index if it doesn't already exist."""
        try:
            # Check if index exists
            self.client.info()
            print(f"Index '{self.index_name}' already exists.")
        except ResponseError:
            schema = [TextField("id", weight=5.0), TextField("name")]
            definition = IndexDefinition(prefix=["doc:"])
            try:
                self.client.create_index(schema, definition=definition)
                print(f"Index '{self.index_name}' created successfully.")
            except ResponseError as e:
                print(f"Failed to create index '{self.index_name}': {str(e)}.")

    def get_index(self):
        """Retrieves and returns the list of existing index names."""
        try:
            indices = self.redis_conn.execute_command("FT._LIST")
            print(f"Existing indices: {indices}")
            return indices
        except ResponseError as e:
            print(f"Error retrieving indices: {str(e)}")

    def delete_index(self):
        """Drops the index and deletes all associated documents."""
        try:
            self.client.dropindex(delete_documents=True)
            print(f"Index '{self.index_name}' deleted successfully.")
        except ResponseError as e:
            print(f"Error deleting index '{self.index_name}': {str(e)}")
