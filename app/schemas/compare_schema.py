from pydantic import BaseModel


class SectionInfo(BaseModel):
    section_number: str
    title: str
    page_number: int | None


class ModifiedSectionInfo(SectionInfo):
    old_hash: str
    new_hash: str


class ComparisonSummary(BaseModel):
    added: int
    removed: int
    modified: int
    unchanged: int


class ComparisonResponse(BaseModel):
    summary: ComparisonSummary
    added: list[SectionInfo]
    removed: list[SectionInfo]
    modified: list[ModifiedSectionInfo]