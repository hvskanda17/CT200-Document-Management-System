from sqlalchemy.orm import Session

from app.models.document import Document
from app.models.version import Version
from app.models.node import Node

from app.utils.hash_generator import generate_hash


class TreePersistenceService:

    def __init__(self, db: Session):
        self.db = db
        self.order_counter = 1

    def save_document(self, document_name, root):

        # -------------------------------
        # Create Document
        # -------------------------------

        document = (
            self.db.query(Document)
            .filter(Document.name == document_name)
            .first()
        )

        if document is None:

            document = Document(
                name=document_name
            )

            self.db.add(document)
            self.db.commit()
            self.db.refresh(document)

        # -------------------------------
        # Create Version
        # -------------------------------

        latest_version = (
            self.db.query(Version)
            .filter(
                Version.document_id == document.id
            )
            .order_by(
                Version.version_number.desc()
            )
            .first()
        )

        version_number = 1

        if latest_version:
            version_number = latest_version.version_number + 1

        version = Version(
            document_id=document.id,
            version_number=version_number
        )

        self.db.add(version)
        self.db.commit()
        self.db.refresh(version)

        # -------------------------------
        # Save Tree
        # -------------------------------

        for child in root.children:

            self.save_node(
                child,
                version.id,
                None
            )

        self.db.commit()

        return version.id

    def save_node(
        self,
        tree_node,
        version_id,
        parent_id
    ):

        db_node = Node(

            version_id=version_id,

            parent_id=parent_id,

            section_number=tree_node.section_number,

            title=tree_node.title,

            level=tree_node.level,

            content=tree_node.content,

            content_hash=generate_hash(
                tree_node.content
            ),

            order_index=self.order_counter,

            page_number=tree_node.page_number
        )

        self.order_counter += 1

        self.db.add(db_node)

        self.db.flush()

        for child in tree_node.children:

            self.save_node(
                child,
                version_id,
                db_node.id
            )