from redis import Redis
from redisearch import Client, TextField, IndexDefinition

def get_redis_client():
    return Redis(host='localhost', port=6379)

def get_redisearch_client():
    client = Client('brands', conn=get_redis_client())
    try:
        client.info()  # Kiểm tra xem index có tồn tại chưa
    except:
        # Nếu chưa tồn tại thì tạo mới
        definition = IndexDefinition(prefix=['brand:'])
        client.create_index([TextField('name')], definition)
    return client
