from pydantic import BaseModel
from typing import List
from datetime import datetime


class SelectionCreate(BaseModel):
    name: str
    version_id: int
    node_ids: List[int]


class SelectionNodeResponse(BaseModel):
    node_id: int
    version_id: int

    class Config:
        from_attributes = True


class SelectionResponse(BaseModel):
    id: int
    name: str
    version_id: int
    created_at: datetime
    node_ids: List[int]
    content: str

    class Config:
        from_attributes = True