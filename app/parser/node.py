import re


class TreeNode:

    def __init__(self, heading="", level=0, node_type="root"):

        self.heading = heading

        self.level = level

        self.node_type = node_type

        self.content = ""

        self.children = []

        self.section_number = ""

        self.title = ""

        if heading:

            self.parse_heading()

    def parse_heading(self):

        match = re.match(r"^(\d+(\.\d+)*)\.?\s+(.*)", self.heading)

        if match:

            self.section_number = match.group(1)

            self.title = match.group(3)

        else:

            self.title = self.heading

    def add_child(self, child):

        self.children.append(child)

    def __repr__(self):

        return f"{self.section_number} {self.title}"