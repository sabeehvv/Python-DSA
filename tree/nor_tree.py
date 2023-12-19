class TreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []

    def add_child(self, child):
        self.children.append(child)


class GeneralTree:
    def __init__(self):
        self.root = None

    def insert(self, data, parent=None):
        if parent is None:
            if self.root is not None:
                raise ValueError("Tree already has a root")
            self.root = TreeNode(data)
        else:
            parent.add_child(TreeNode(data))

    def traverse(self):
        if self.root is None:
            print("Tree is empty")
        else:
            self._traverse_helper(self.root)

    def _traverse_helper(self, node):
        print(node.data)
        for child in node.children:
            self._traverse_helper(child)


gt = GeneralTree()

gt.insert("A")
gt.insert("B", parent=gt.root)
gt.insert("C", parent=gt.root)
gt.insert("D", parent=gt.root.children[0])
gt.insert("E", parent=gt.root.children[0])
gt.insert("F", parent=gt.root.children[1])
gt.traverse()

