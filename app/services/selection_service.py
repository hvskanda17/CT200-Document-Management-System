from sqlalchemy.orm import Session

from app.models.selection import Selection
from app.models.selection_node import SelectionNode
from app.models.node import Node

from app.schemas.selection_schema import (
    SelectionCreate,
    SelectionResponse
)


class SelectionService:

    @staticmethod
    def create_selection(
        db: Session,
        selection_data: SelectionCreate
    ) -> SelectionResponse:

        # Validate node IDs
        nodes = (
            db.query(Node)
            .filter(Node.id.in_(selection_data.node_ids))
            .all()
        )

        if len(nodes) != len(selection_data.node_ids):
            raise ValueError("One or more node IDs are invalid.")

        # Create Selection
        selection = Selection(
            name=selection_data.name,
            version_id=selection_data.version_id
        )

        db.add(selection)
        db.commit()
        db.refresh(selection)

        # Store selected nodes
        for node in nodes:

            selection_node = SelectionNode(
                selection_id=selection.id,
                node_id=node.id,
                version_id=selection_data.version_id
            )

            db.add(selection_node)

        db.commit()

        return SelectionResponse(
            id=selection.id,
            name=selection.name,
            version_id=selection.version_id,
            created_at=selection.created_at,
            node_ids=selection_data.node_ids,
            content=""
        )
    @staticmethod
    def get_selection(
    db: Session,
    selection_id: int
    ):

        selection = (
        db.query(Selection)
        .filter(Selection.id == selection_id)
        .first()
    )

        if selection is None:
            return None

        selection_nodes = (
        db.query(SelectionNode)
        .filter(
            SelectionNode.selection_id == selection_id
        )
        .all()
        )

        node_ids = []

        content_parts = []

        for selection_node in selection_nodes:

            node_ids.append(selection_node.node_id)

            node = (
            db.query(Node)
            .filter(Node.id == selection_node.node_id)
            .first()
            )

            if node:
                content_parts.append(node.content)

        return SelectionResponse(
        id=selection.id,
        name=selection.name,
        version_id=selection.version_id,
        created_at=selection.created_at,
        node_ids=node_ids,
        content="\n\n".join(content_parts)
    )