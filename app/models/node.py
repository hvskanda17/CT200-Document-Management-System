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

    heading = Column(String)

    level = Column(Integer)

    body = Column(Text)

    content_hash = Column(String)