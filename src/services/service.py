from src.data.database import Redisearch
from src.schemas.schema import User


def insert(user: User):
    redisearch = Redisearch("idx:test")
    redisearch.client.redis.hset(f"doc:{user.id}", mapping=user)
    print("Succeed to insert a user.")


def delete(user_id: str):
    redisearch = Redisearch("idx:test")
    redisearch.client.delete(user_id)


def update(user_id: str, user: User):
    redisearch = Redisearch("idx:test")
    redisearch.client.hset(user_id, mapping={"name": user.name})


# def search(self, query: str):
#     query = Query(q).return_fields("name")
#     results = redisearch_client.search(query)
#     brands = [{"id": doc.id, "name": doc.name} for doc in results.docs]
#     return {"brands": brands}

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
