from contextlib import asynccontextmanager
from fastapi import FastAPI

# from fastapi_cache import FastAPICache
# from fastapi_cache.backends.inmemory import InMemoryBackend
from src.routes import route


# @asynccontextmanager
# async def lifespan_context_manager(_):
#     """
#     Context manager for the FastAPI app lifespan.

#     Initializes  FastAPICache with an InMemoryBackend for the duration of the app's lifespan.
#     """
#     FastAPICache.init(InMemoryBackend())
#     yield

app = FastAPI(
    title="python-samples-fastapi-restful",
    description="🧪 Proof of Concept for a RESTful API made with Python 3 and FastAPI",
    version="1.0.0",
)

app.include_router(route.api_router)
