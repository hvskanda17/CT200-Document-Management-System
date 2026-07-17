from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from app.database.database import get_db

from app.models.selection import Selection
from app.models.selection_node import SelectionNode
from app.models.node import Node

from app.schemas.qa_schema import QAResponse, QAPair
from app.services.gemini_service import GeminiService

router = APIRouter(
    prefix="/api",
    tags=["QA Generation"]
)


@router.post(
    "/selections/{selection_id}/generate-qa",
    response_model=QAResponse
)
def generate_qa(
    selection_id: int,
    db: Session = Depends(get_db)
):

    selection = (
        db.query(Selection)
        .filter(Selection.id == selection_id)
        .first()
    )

    if selection is None:
        raise HTTPException(
            status_code=404,
            detail="Selection not found"
        )

    selection_nodes = (
        db.query(SelectionNode)
        .filter(
            SelectionNode.selection_id == selection_id
        )
        .all()
    )

    content_parts = []

    for selection_node in selection_nodes:

        node = (
            db.query(Node)
            .filter(Node.id == selection_node.node_id)
            .first()
        )

        if node:
            content_parts.append(node.content)

    content = "\n\n".join(content_parts)

    qa_pairs = GeminiService.generate_qa(content)

    return QAResponse(
        selection_id=selection_id,
        test_cases=[
            QAPair(
                question=item["question"],
                answer=item["answer"]
            )
            for item in qa_pairs
        ]
    )