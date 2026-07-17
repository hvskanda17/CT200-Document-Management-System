from pydantic import BaseModel
from typing import List


class QAPair(BaseModel):
    question: str
    answer: str


class QAResponse(BaseModel):
    selection_id: int
    test_cases: List[QAPair]