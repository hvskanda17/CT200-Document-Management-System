from fastapi import FastAPI

from app.database.database import engine, Base

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


@app.get("/")
def root():
    return {
        "message": "CT-200 Backend Running Successfully"
    }