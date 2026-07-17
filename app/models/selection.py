from sqlalchemy import Column, Integer, String, DateTime, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from app.database.database import Base


class Selection(Base):
    __tablename__ = "selections"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String, nullable=False)

    version_id = Column(
        Integer,
        ForeignKey("versions.id"),
        nullable=False
    )

    created_at = Column(
        DateTime(timezone=True),
        server_default=func.now()
    )

    version = relationship("Version")

    selection_nodes = relationship(
        "SelectionNode",
        back_populates="selection",
        cascade="all, delete-orphan"
    )