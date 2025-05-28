"""This module contains common dependencies used in the application"""

from typing import Literal

from app.common.types import PaginationParamsType
from app.core.database import SessionLocal


def get_db():
    """
    This function yields a db
    """
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def pagination_params(
    q: str | None = None,
    page: int = 1,
    size: int = 10,
    order_by: Literal["desc", "asc"] = "desc",
):
    """
    Helper Dependency for pagination
    """
    return PaginationParamsType(q=q, page=page, size=size, order_by=order_by)
