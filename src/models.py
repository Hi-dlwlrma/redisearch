from redisearch import Document
from redis_client import get_redisearch_client

class Brand:
    def __init__(self):
        self.client = get_redisearch_client()

    def add_brand(self, brand_id, name):
        # Thêm một brand vào Redisearch
        doc = Document(brand_id, name=name)
        self.client.add_document(doc)
        return {'id': brand_id, 'name': name}

    def delete_brand(self, brand_id):
        # Xóa một brand khỏi Redisearch
        self.client.delete_document(brand_id)
        return {'status': 'deleted', 'id': brand_id}

    def update_brand(self, brand_id, name):
        # Cập nhật một brand trong Redisearch
        self.client.replace_document(brand_id, name=name)
        return {'id': brand_id, 'name': name}

    def search_brand(self, query):
        # Tìm kiếm brand trong Redisearch
        result = self.client.search(query)
        brands = [{'id': doc.id, 'name': doc.name} for doc in result.docs]
        return brands
