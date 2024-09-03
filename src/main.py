from fastapi import FastAPI

from src.routes import route

if __name__ == "__main__":
    app = FastAPI(
        title="python-samples-fastapi-restful",
        description="🧪 Proof of Concept for a RESTful API made with Python 3 and FastAPI",
        version="1.0.0",
    )

    app.include_router(route.api_router)
