from pydantic import BaseModel


class DocumentResponse(BaseModel):
    id: int
    name: str

    class Config:
        from_attributes = True


class VersionResponse(BaseModel):
    id: int
    version_number: int

    class Config:
        from_attributes = True


class NodeResponse(BaseModel):
    id: int
    section_number: str
    title: str
    level: int
    content: str | None
    page_number: int | None

    class Config:
        from_attributes = True