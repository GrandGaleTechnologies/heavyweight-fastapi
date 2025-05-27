"""This module contains the API endpoints for the example module."""

from fastapi import APIRouter

from app.common.annotations import PaginationParams
from app.example_module import schemas

router = APIRouter()


NAMES = [
    {
        "first_name": "Alice",
        "last_name": "Wonderland",
    },
    {
        "first_name": "Bob",
        "last_name": "Builder",
    },
    {
        "first_name": "Charlie",
        "last_name": "Chaplin",
    },
    {
        "first_name": "Dora",
        "last_name": "Explorer",
    },
]


@router.get(
    "",
    summary="Example Endpoint",
    response_description="The paginated list of names",
    status_code=200,
    response_model=schemas.NameResponse,
)
async def route_example_endpoint(pagination: PaginationParams):
    """
    This is an example endpoint
    """
    page = pagination.page
    size = pagination.size

    names = NAMES[(page - 1) * size : page * size]

    response = {
        "data": names,
        "meta": {
            "total_no_items": len(NAMES),
            "total_no_pages": len(NAMES) // size,
            "page": page,
            "size": size,
            "count": len(names),
            "has_next_page": page < len(NAMES) // size,
            "has_prev_page": page > 1,
        },
    }

    return response
