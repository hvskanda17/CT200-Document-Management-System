from app.parser.pdf_reader import PDFReader
from app.parser.hierarchy_builder import HierarchyBuilder


def print_tree(node, indent=0):
    """
    Recursively prints the document hierarchy.
    """

    if node.node_type != "root":

        print(
            " " * indent
            + f"{node.section_number} {node.title}"
        )

        if node.content:
            print(
                " " * (indent + 4)
                + "Content: "
                + node.content[:80]
                + ("..." if len(node.content) > 80 else "")
            )

    for child in node.children:
        print_tree(child, indent + 4)


def count_nodes(node):
    """
    Counts all nodes in the hierarchy.
    """

    count = 0

    if node.node_type != "root":
        count += 1

    for child in node.children:
        count += count_nodes(child)

    return count


def main():

    print("=" * 70)
    print("READING PDF...")
    print("=" * 70)

    reader = PDFReader("data/ct200_manual.pdf")

    blocks = reader.extract_blocks()

    print(f"\nTotal Extracted Blocks : {len(blocks)}")

    print("\n" + "=" * 70)
    print("BUILDING HIERARCHY...")
    print("=" * 70)

    builder = HierarchyBuilder(blocks)

    root = builder.build_tree()

    print("\nHierarchy:\n")

    print_tree(root)

    print("\n" + "=" * 70)

    print(f"Total Nodes : {count_nodes(root)}")

    print("=" * 70)


if __name__ == "__main__":
    main()