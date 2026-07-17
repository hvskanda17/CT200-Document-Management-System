from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.schemas.selection_schema import (
    SelectionCreate,
    SelectionResponse
)
from app.services.selection_service import SelectionService

router = APIRouter(
    prefix="/api",
    tags=["Selections"]
)


@router.post(
    "/selections",
    response_model=SelectionResponse
)
def create_selection(
    selection: SelectionCreate,
    db: Session = Depends(get_db)
):
    try:
        return SelectionService.create_selection(db, selection)

    except ValueError as e:
        raise HTTPException(
            status_code=400,
            detail=str(e)
        )
@router.get(
    "/selections/{selection_id}",
    response_model=SelectionResponse
)
def get_selection(
    selection_id: int,
    db: Session = Depends(get_db)
):

    selection = SelectionService.get_selection(
        db,
        selection_id
    )

    if selection is None:
        raise HTTPException(
            status_code=404,
            detail="Selection not found"
        )

    return selection