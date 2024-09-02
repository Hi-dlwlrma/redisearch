from src.core.database import Redisearch
from src.schemas.models import Brand


class Handler:
    def __init__(self) -> None:
        self.redisearch = Redisearch("idx:test")

    def insert(self, brand: Brand):
        self.redisearch.client.redis.hset(f"doc:{brand.id}", mapping=brand)
        print("Succeed to insert a brand.")
        return {"message": "Brand created successfully", "brand": brand}

    def delete(self, brand_id: str):
        self.redisearch.client.delete(brand_id)
        return {"message": "Brand deleted successfully"}

    def update(self, brand_id: str, brand: Brand):
        self.redisearch.client.hset(brand_id, mapping={"name": brand.name})
        return {"message": "Brand updated successfully", "brand": brand}

    def search(self, query: str):
        query = Query(q).return_fields("name")
        results = redisearch_client.search(query)
        brands = [{"id": doc.id, "name": doc.name} for doc in results.docs]
        return {"brands": brands}

    # def search(self):
    #     offset = 0
    #     limit = 10
    #     queryString = ""

    #     if request.args.get("offset"):
    #         offset = int(request.args.get("offset"))

    #     if request.args.get("limit"):
    #         limit = int(request.args.get("limit"))

    #     if request.args.get("q"):
    #         queryString = request.args.get("q")
    #     q = Query(queryString).with_scores().paging(offset, limit)
    #     if request.args.get("sortby"):
    #         ascending = True
    #         if request.args.get("ascending"):
    #             ascending = (
    #                 request.args.get("ascending").lower() == "true"
    #                 or request.args.get("ascending") == "1"
    #             )

    #         q.sort_by(request.args.get("sortby"), asc=ascending)

    #     searchResult = conn.ft(index_name=redis_index).search(q)

    #     dictResult = {
    #         "meta": {
    #             "totalResults": getattr(searchResult, "total"),
    #             "offset": offset,
    #             "limit": limit,
    #             "queryString": queryString,
    #         },
    #         "docs": self.docs_to_dict(searchResult.docs),
    #     }

    #     return dictResult

    def docs_to_dict(self, docs):
        reslist = []
        for doc in docs:
            meta = {"id": getattr(doc, "id"), "score": getattr(doc, "score")}
            fields = {}
            for field in dir(doc):
                if field.startswith("__") or field == "id" or field == "score":
                    continue
                fields.update({field: getattr(doc, field)})
            ddict = {"meta": meta, "fields": fields}
            reslist.append(ddict)
        return reslist
