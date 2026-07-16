from app.database.database import SessionLocal

from app.parser.pdf_reader import PDFReader
from app.parser.hierarchy_builder import HierarchyBuilder

from app.services.tree_persistence import TreePersistenceService


db = SessionLocal()

reader = PDFReader("data/ct200_manual.pdf")

blocks = reader.extract_blocks()

builder = HierarchyBuilder(blocks)

root = builder.build_tree()

service = TreePersistenceService(db)

version_id = service.save_document(
    "CT200 Manual",
    root
)

print(f"Saved Version : {version_id}")

db.close()