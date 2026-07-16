class TreeNode:
    def __init__(self, title="", level=0, node_type="root"):
        self.title = title
        self.level = level
        self.node_type = node_type

        self.content = ""
        self.children = []

    def add_child(self, child):
        self.children.append(child)

    def __repr__(self):
        return f"{self.node_type}: {self.title}"