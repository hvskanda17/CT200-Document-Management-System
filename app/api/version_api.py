from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.services.version_compare_service import VersionCompareService
from app.schemas.compare_schema import ComparisonResponse

router = APIRouter(prefix="/api")


@router.get(
    "/versions/{version1_id}/compare/{version2_id}",
    response_model=ComparisonResponse
)
def compare_versions(
    version1_id: int,
    version2_id: int,
    db: Session = Depends(get_db)
):

    service = VersionCompareService(db)

    try:
        return service.compare_versions(
            version1_id,
            version2_id
        )

    except ValueError as e:
        raise HTTPException(
            status_code=404,
            detail=str(e)
        )