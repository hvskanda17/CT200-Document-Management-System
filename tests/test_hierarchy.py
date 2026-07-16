from app.parser.pdf_reader import PDFReader
from app.parser.hierarchy_builder import HierarchyBuilder

reader = PDFReader("data/ct200_manual.pdf")

blocks = reader.extract_blocks()

builder = HierarchyBuilder(blocks)

nodes = builder.merge_paragraphs()

for node in nodes[:20]:
    print(node)