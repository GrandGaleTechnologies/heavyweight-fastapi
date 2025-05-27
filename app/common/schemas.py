"""This module contains the schemas used in the application."""

from typing import Any

from pydantic import BaseModel, Field


class ResponseSchema(BaseModel):
    """
    Generic response schema for the application.
    """

    status: str = Field(description="The status of the request", default="success")
    data: Any = Field(description="The data")


class PaginationSchema(BaseModel):
    """
    Generic paginated response schema for the application.
    """

    total_no_items: int = Field(description="The total number of items available")
    total_no_pages: int = Field(description="The total number of pages")
    page: int = Field(description="The current page number")
    size: int = Field(description="Max number of items to return per page")
    count: int = Field(description="The number of items returned")
    has_next_page: bool = Field(description="Indicates if there is a next page")
    has_prev_page: bool = Field(description="Indicates if there is a previous page")


class PaginatedResponseSchema(ResponseSchema):
    """
    Generic schema for paginated responses
    """

    meta: PaginationSchema = Field(description="The pagination metadata")
