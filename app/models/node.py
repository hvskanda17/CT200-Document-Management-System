from sqlalchemy import Column, Integer, String, ForeignKey, Text

from app.database.database import Base


class Node(Base):
    __tablename__ = "nodes"

    id = Column(Integer, primary_key=True, index=True)

    version_id = Column(
        Integer,
        ForeignKey("versions.id"),
        nullable=False
    )

    parent_id = Column(
        Integer,
        ForeignKey("nodes.id"),
        nullable=True
    )

    section_number = Column(String, nullable=False)

    title = Column(String, nullable=False)

    level = Column(Integer, nullable=False)

    content = Column(Text)

    content_hash = Column(String)

    order_index = Column(Integer)

    page_number = Column(Integer)