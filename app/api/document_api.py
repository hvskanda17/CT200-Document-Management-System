from fastapi import APIRouter, Depends
from fastapi import HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.services.document_service import DocumentService

from app.schemas.document_schema import (
    DocumentResponse,
    VersionResponse,
    NodeResponse,
)

router = APIRouter(prefix="/api")

@router.get(
    "/documents",
    response_model=list[DocumentResponse]
)
def get_documents(db: Session = Depends(get_db)):

    service = DocumentService(db)

    return service.get_documents()


@router.get(
    "/documents/{document_id}/versions",
    response_model=list[VersionResponse]
)
def get_versions(
    document_id: int,
    db: Session = Depends(get_db),
):

    service = DocumentService(db)

    return service.get_versions(document_id)


@router.get(
    "/nodes/{node_id}",
    response_model=NodeResponse
)
def get_node(
    node_id: int,
    db: Session = Depends(get_db),
):

    service = DocumentService(db)

    node = service.get_node(node_id)

    if node is None:
        raise HTTPException(
            status_code=404,
            detail="Node not found"
        )

    return node