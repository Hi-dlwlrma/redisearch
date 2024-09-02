from redis import Redis, ResponseError
from redisearch import Client, IndexDefinition, TextField
from src.config import *


class Redisearch:
    def __init__(self, index_name=None):
        self.index_name = index_name
        self.redis_conn = Redis(host=REDIS_HOST, port=REDIS_PORT, decode_responses=True)
        self.client = Client(self.index_name)

    def create_index(self):
        try:
            self.client.info()
        except ResponseError:
            try:
                schema = (TextField("id", weight=5.0), TextField("name"))
                definition = IndexDefinition(prefix=["doc:"])
                self.client.create_index(schema, definition=definition)
                print("Succeed to create an index.")
            except ResponseError:
                self.client.dropindex(delete_documents=True)
                print("Failed to create an index.")

    def get_index(self):
        index_names = self.redis_conn.execute_command("FT._LIST")
        print("All index names: ", index_names)

    def delete_index(self):
        self.client.dropindex(delete_documents=True)
        return self.client
