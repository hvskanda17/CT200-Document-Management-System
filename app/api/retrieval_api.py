from fastapi import APIRouter, HTTPException, Depends
from sqlalchemy.orm import Session

from app.database.database import get_db
from app.database.mongo import generated_collection
from app.models.node import Node

router = APIRouter(prefix="/api/generated", tags=["Generated QA"])


@router.get("/{selection_id}")
def get_generated(selection_id: int, db: Session = Depends(get_db)):

    generation = generated_collection.find_one(
        {"selection_id": selection_id},
        sort=[("generated_at", -1)]
    )

    if generation is None:
        raise HTTPException(status_code=404, detail="No generated QA found")

    changed_nodes = []

    for node_id, old_hash in generation["node_hashes"].items():

        node = db.query(Node).filter(Node.id == int(node_id)).first()

        if node and node.content_hash != old_hash:
            changed_nodes.append(node.id)

    return {
        "selection_id": selection_id,
        "generated_at": generation["generated_at"],
        "qa_pairs": generation["qa_pairs"],
        "is_stale": len(changed_nodes) > 0,
        "changed_nodes": changed_nodes
    }
@router.get("/node/{node_id}")
def get_generated_by_node(node_id: int):

    generations = list(
        generated_collection.find(
            {"node_ids": node_id},
            {"_id": 0}
        )
    )

    if not generations:
        raise HTTPException(
            status_code=404,
            detail="No generated QA found for this node"
        )

    response = []

    for generation in generations:

        response.append({
            "selection_id": generation["selection_id"],
            "version_id": generation["version_id"],
            "generated_at": generation["generated_at"],
            "qa_pairs": generation["qa_pairs"]
        })

    return {
        "node_id": node_id,
        "count": len(response),
        "generations": response
    }