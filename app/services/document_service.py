from sqlalchemy.orm import Session

from app.models.document import Document
from app.models.version import Version
from app.models.node import Node


class DocumentService:

    def __init__(self, db: Session):
        self.db = db

    def get_documents(self):
        return self.db.query(Document).all()

    def get_versions(self, document_id):
        return (
            self.db.query(Version)
            .filter(Version.document_id == document_id)
            .all()
        )

    def get_node(self, node_id):
        return (
            self.db.query(Node)
            .filter(Node.id == node_id)
            .first()
        )