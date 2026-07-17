from sqlalchemy import Column, Integer, ForeignKey
from sqlalchemy.orm import relationship

from app.database.database import Base


class SelectionNode(Base):
    __tablename__ = "selection_nodes"

    id = Column(Integer, primary_key=True, index=True)

    selection_id = Column(
        Integer,
        ForeignKey("selections.id"),
        nullable=False
    )

    node_id = Column(
        Integer,
        ForeignKey("nodes.id"),
        nullable=False
    )

    version_id = Column(
        Integer,
        ForeignKey("versions.id"),
        nullable=False
    )

    selection = relationship(
        "Selection",
        back_populates="selection_nodes"
    )

    node = relationship("Node")

    version = relationship("Version")