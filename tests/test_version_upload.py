from app.database.database import SessionLocal

from app.parser.pdf_reader import PDFReader
from app.parser.hierarchy_builder import HierarchyBuilder

from app.services.tree_persistence import TreePersistenceService


def main():

    db = SessionLocal()

    print("=" * 60)
    print("READING VERSION 2 PDF")
    print("=" * 60)

    reader = PDFReader("data/ct200_manual_v2.pdf")

    blocks = reader.extract_blocks()

    builder = HierarchyBuilder(blocks)

    root = builder.build_tree()

    service = TreePersistenceService(db)

    version_id = service.save_document(
        "CT200 Manual",
        root
    )

    print()

    print(f"Created Version : {version_id}")

    db.close()


if __name__ == "__main__":
    main()