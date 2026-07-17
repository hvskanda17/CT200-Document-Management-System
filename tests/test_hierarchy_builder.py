import pytest

from app.parser.hierarchy_builder import HierarchyBuilder


def test_heading_detection():

    heading = {
        "text": "1 Introduction",
        "font_name": "Arial-BoldMT",
        "page": 1
    }

    non_heading = {
        "text": "Introduction",
        "font_name": "Arial",
        "page": 1
    }

    builder = HierarchyBuilder([])

    assert builder.is_heading(heading) is True
    assert builder.is_heading(non_heading) is False


def test_deep_nested_hierarchy():

    blocks = [

        {"text": "1 Introduction", "font_name": "Arial-BoldMT", "page": 1},
        {"text": "Introduction Content", "font_name": "Arial", "page": 1},

        {"text": "1.1 Scope", "font_name": "Arial-BoldMT", "page": 1},
        {"text": "Scope Content", "font_name": "Arial", "page": 1},

        {"text": "1.1.1 Device", "font_name": "Arial-BoldMT", "page": 1},
        {"text": "Device Content", "font_name": "Arial", "page": 1},

        {"text": "1.1.1.1 Battery", "font_name": "Arial-BoldMT", "page": 1},
        {"text": "Battery Content", "font_name": "Arial", "page": 1},
    ]

    root = HierarchyBuilder(blocks).build_tree()

    intro = root.children[0]
    scope = intro.children[0]
    device = scope.children[0]
    battery = device.children[0]

    assert intro.heading == "1 Introduction"
    assert scope.heading == "1.1 Scope"
    assert device.heading == "1.1.1 Device"
    assert battery.heading == "1.1.1.1 Battery"

    assert intro.content == "Introduction Content"
    assert scope.content == "Scope Content"
    assert device.content == "Device Content"
    assert battery.content == "Battery Content"


def test_ignore_text_before_first_heading():

    blocks = [

        {"text": "CT-200 USER MANUAL", "font_name": "Arial-BoldMT", "page": 1},
        {"text": "Revision 1", "font_name": "Arial", "page": 1},

        {"text": "1 Introduction", "font_name": "Arial-BoldMT", "page": 2},
        {"text": "Introduction starts here.", "font_name": "Arial", "page": 2},
    ]

    root = HierarchyBuilder(blocks).build_tree()

    assert len(root.children) == 1
    assert root.children[0].heading == "1 Introduction"
    assert root.children[0].content == "Introduction starts here."


def test_duplicate_headings_are_kept_separate():

    blocks = [

        {"text": "1 Safety", "font_name": "Arial-BoldMT", "page": 1},
        {"text": "Original safety instructions.", "font_name": "Arial", "page": 1},

        {"text": "1 Safety", "font_name": "Arial-BoldMT", "page": 5},
        {"text": "Updated safety instructions.", "font_name": "Arial", "page": 5},
    ]

    root = HierarchyBuilder(blocks).build_tree()

    assert len(root.children) == 2

    assert root.children[0].heading == "1 Safety"
    assert root.children[0].content == "Original safety instructions."

    assert root.children[1].heading == "1 Safety"
    assert root.children[1].content == "Updated safety instructions."


def test_multiple_paragraphs_are_merged():

    blocks = [

        {"text": "1 Overview", "font_name": "Arial-BoldMT", "page": 1},

        {"text": "Paragraph One.", "font_name": "Arial", "page": 1},
        {"text": "Paragraph Two.", "font_name": "Arial", "page": 1},
        {"text": "Paragraph Three.", "font_name": "Arial", "page": 1},
    ]

    root = HierarchyBuilder(blocks).build_tree()

    assert (
        root.children[0].content ==
        "Paragraph One. Paragraph Two. Paragraph Three."
    )


def test_complex_tree_structure():

    blocks = [

        {"text": "1 A", "font_name": "Arial-BoldMT", "page": 1},
        {"text": "A Content", "font_name": "Arial", "page": 1},

        {"text": "1.1 B", "font_name": "Arial-BoldMT", "page": 1},
        {"text": "B Content", "font_name": "Arial", "page": 1},

        {"text": "1.1.1 C", "font_name": "Arial-BoldMT", "page": 1},
        {"text": "C Content", "font_name": "Arial", "page": 1},

        {"text": "1.2 D", "font_name": "Arial-BoldMT", "page": 1},
        {"text": "D Content", "font_name": "Arial", "page": 1},

        {"text": "2 E", "font_name": "Arial-BoldMT", "page": 1},
        {"text": "E Content", "font_name": "Arial", "page": 1},
    ]

    root = HierarchyBuilder(blocks).build_tree()

    assert len(root.children) == 2

    section_a = root.children[0]
    section_e = root.children[1]

    assert section_a.heading == "1 A"
    assert section_e.heading == "2 E"

    assert len(section_a.children) == 2

    assert section_a.children[0].heading == "1.1 B"
    assert section_a.children[1].heading == "1.2 D"

    assert section_a.children[0].children[0].heading == "1.1.1 C"

    assert section_a.content == "A Content"
    assert section_a.children[0].content == "B Content"
    assert section_a.children[0].children[0].content == "C Content"
    assert section_a.children[1].content == "D Content"
    assert section_e.content == "E Content"