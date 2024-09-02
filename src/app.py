from fastapi import FastAPI
from src.routers import crud

app = FastAPI()


@app.post("/brands/")
async def create_brand(brand: crud.Brand):
    return crud.create_brand(brand)


@app.delete("/brands/{brand_id}")
async def delete_brand(brand_id: str):
    return crud.delete_brand(brand_id)


@app.put("/brands/{brand_id}")
async def update_brand(brand_id: str, brand: crud.Brand):
    return crud.update_brand(brand_id, brand)


@app.get("/brands/search/")
async def search_brands(q: str):
    return crud.search_brands(q)
