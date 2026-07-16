from app.parser.pdf_reader import PDFReader
from app.parser.hierarchy_builder import HierarchyBuilder


def print_tree(node, indent=0):

    if node.title != "ROOT":
        print(" " * indent + node.title)

    for child in node.children:
        print_tree(child, indent + 4)


reader = PDFReader("data/ct200_manual.pdf")

blocks = reader.extract_blocks()

builder = HierarchyBuilder(blocks)

root = builder.build_tree()

print_tree(root)