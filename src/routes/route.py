from typing import Any, Optional
from fastapi import APIRouter
from fastapi.encoders import jsonable_encoder
from starlette import status
from starlette.responses import JSONResponse

from src.schemas import schema, response
from src.services import service

api_router = APIRouter()


def success_response(response_data: Optional[Any] = None) -> JSONResponse:
    """
    Returns a JSON response with the given status code and the given data.
    :param response_data: The data to be returned.
    :return: A JSON response with the given status code and the given data.
    """
    response_json = {"success": True}

    if response_data is not None:
        response_json["data"] = jsonable_encoder(response_data)

    return JSONResponse(response_json, status_code=status.HTTP_200_OK)


def error_response(
    errors: Optional[Any] = None,
    status_code: int = status.HTTP_500_INTERNAL_SERVER_ERROR,
) -> JSONResponse:
    """
    Returns a JSON response with the given status code and the given errors.
    :param errors: The errors to be returned.
    :param status_code: The status code of the response.
    :return: A JSON response with the given status code and the given errors.
    """
    response_json = {"success": False}
    if errors is not None:
        response_json["errors"] = jsonable_encoder(errors)

    return JSONResponse(response_json, status_code=status_code)


@api_router.post("/insert", response_model=response.MovieResponse)
async def insert_movie(request: schema.Movie) -> JSONResponse:
    response = service.insert(request)
    print(response)
    return success_response(response)


@api_router.put("/update", response_model=response.MovieResponse)
async def update_movie(request_id: str, request: schema.Movie) -> JSONResponse:
    response = service.update(request_id, request)
    print(response)
    return success_response(response)


@api_router.delete("/delete", response_model=response.BaseResponse)
async def delete_movie(request_id: str) -> JSONResponse:
    service.delete(request_id)
    return success_response()


@api_router.get("/search", response_model=response.MovieListResponse)
async def search_movie(search_term: str, field: str) -> JSONResponse:
    response = service.search(search_term, field)
    return success_response(response)
