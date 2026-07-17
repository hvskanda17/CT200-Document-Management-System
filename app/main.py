from fastapi import FastAPI
from app.api.document_api import router as document_router
from app.api.version_api import router as version_router
from app.database.database import engine, Base
from app.models.selection import Selection
from app.models.selection_node import SelectionNode
from app.api.selection_api import router as selection_router
from app.models import (
    document,
    version,
    node,
    selection,
    selection_node
)

Base.metadata.create_all(bind=engine)

app = FastAPI(
    title="CT-200 Document Management API",
    version="1.0.0"
)
app.include_router(document_router)
app.include_router(version_router)
app.include_router(selection_router)