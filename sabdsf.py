def is_bst(arr):
    def check_binary(node):
        nonlocal prev_node
        if node is None:
            return True
        if not check_binary(node.left):
            return False
        if prev_node is not None and node.data <= prev_node.data:
            return False
        return check_binary(node.right)
    prev_node = None

    return chech_binary(arr)

class treenode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class binarytree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = treenode(data)
        else:
            self.inser_helper(self.root,data)

    def inser_helper(self,node,data):
        if node.data >= data:
            if node
