class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)


root = TreeNode("A")
child1 = TreeNode("B")
child2 = TreeNode("C")
child3 = TreeNode("D")
child4 = TreeNode("E")


root.add_child(child1)
child3.add_child(child2)
child1.add_child(child3)
child1.add_child(child4)


def traverse(node):
    print(node.data)
    for child in node.children:
        traverse(child)

traverse(root)
