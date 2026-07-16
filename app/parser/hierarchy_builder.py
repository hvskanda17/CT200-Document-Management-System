import re

from app.parser.node import TreeNode


class HierarchyBuilder:

    def __init__(self, blocks):
        self.blocks = blocks

    def is_heading(self, block):

        text = block["text"].strip()

        heading_pattern = r"^\d+(\.\d+)*\.?\s+"

        if not re.match(heading_pattern, text):
            return False

        return "Bold" in block["font_name"]

    def get_heading_level(self, heading):

        number = heading.split()[0]

        number = number.rstrip(".")

        return number.count(".") + 1

    def build_tree(self):

        root = TreeNode("ROOT", 0, "root")

        stack = [root]

        current_node = None

        for block in self.blocks:

            text = block["text"].strip()

            if not text:
                continue

            # Ignore document title before first numbered heading
            if current_node is None and not self.is_heading(block):
                continue

            if self.is_heading(block):

                level = self.get_heading_level(text)

                node = TreeNode(
                    heading=text,
                    level=level,
                    node_type="heading"
                )

                while stack and stack[-1].level >= level:
                    stack.pop()

                stack[-1].add_child(node)

                stack.append(node)

                current_node = node

            else:

                if current_node:

                    if current_node.content:
                        current_node.content += " "

                    current_node.content += text

        return root