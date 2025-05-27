from typing import Annotated

from fastapi import Depends
from sqlalchemy.orm import Session

from app.common.dependencies import get_db, pagination_params
from app.common.types import PaginationParamsType

DatabaseSession = Annotated[Session, Depends(get_db)]
PaginationParams = Annotated[PaginationParamsType, Depends(pagination_params)]
