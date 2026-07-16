from sqlalchemy import Column, Integer, String
from app.database.database import Base


class Selection(Base):
    __tablename__ = "selections"

    id = Column(Integer, primary_key=True, index=True)

    name = Column(String)