class TreeNode:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


def is_bst(root):
    def inorder_traversal(node):
        nonlocal prev_node
        if node is None:
            return True
        
        if not inorder_traversal(node.left):
            return False
        
        if prev_node is not None and prev_node.val >= node.val:
            return False
        
        prev_node = node
        return inorder_traversal(node.right)

    prev_node = None
    return inorder_traversal(root)



root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(6)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)
root.right.left = TreeNode(5)
root.right.right = TreeNode(7)

is_valid_bst = is_bst(root)
print(is_valid_bst)