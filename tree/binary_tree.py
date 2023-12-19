class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class TreeNode1:
    def __init__(self, value):
        self.val = value
        self.left = None
        self.right = None


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root is None:
            self.root = TreeNode(data)
        else:
            self._insert_helper(self.root, data)

    def _insert_helper(self, node, data):
        if data < node.data:
            if node.left is None:
                node.left = TreeNode(data)
            else:
                self._insert_helper(node.left, data)
        else:
            if node.right is None:
                node.right = TreeNode(data)
            else:
                self._insert_helper(node.right, data)

    def contains(self, data):
        return self._contains_helper(self.root, data)

    def _contains_helper(self, node, data):
        if node is None:
            return False
        if node.data == data:
            return True
        if data < node.data:
            return self._contains_helper(node.left, data)
        return self._contains_helper(node.right, data)

    def delete(self, data):
        self.root = self._delete_helper(self.root, data)

    def _delete_helper(self, node, data):

        if node is None:
            return node
        if data < node.data:
            node.left = self._delete_helper(node.left, data)
        elif data > node.data:
            node.right = self._delete_helper(node.right, data)
        else:
            if node.left is None:
                temp = node.right
                node = None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            else:
                temp = self._get_min_value_node(node.right)
                node.data = temp.data
                node.right = self._delete_helper(node.right, temp.data)
        return node

    def _get_min_value_node(self, node):
        current = node
        while current.left is not None:
            current = current.left
        return current

    def inorder_traversal(self):
        self._inorder_traversal_helper(self.root)

    def _inorder_traversal_helper(self, node):
        if node is not None:
            self._inorder_traversal_helper(node.left)
            print(node.data, end=" ")
            self._inorder_traversal_helper(node.right)

    def preorder_traversal(self):
        self._preorder_traversal_helper(self.root)

    def _preorder_traversal_helper(self, node):
        if node is not None:
            print(node.data, end=" ")
            self._preorder_traversal_helper(node.left)
            self._preorder_traversal_helper(node.right)

    def postorder_traversal(self):
        self._postorder_traversal_helper(self.root)

    def _postorder_traversal_helper(self, node):
        if node is not None:
            self._postorder_traversal_helper(node.left)
            self._postorder_traversal_helper(node.right)
            print(node.data, end=" ")

    def is_bst_check(self):
        return self.is_bst(self.root)

    def is_bst(self, node1):
        def inorder_traversal(node):
            nonlocal prev_node
            if node is None:
                return True

            inorder_traversal(node.left)

            if prev_node is not None and prev_node.val >= node.val:
                return False

            prev_node = node

            return inorder_traversal(node.right)

        prev_node = None
        return inorder_traversal(node1)


bst = BinarySearchTree()
bst.insert(5)
bst.insert(3)
bst.insert(7)
bst.insert(2)
bst.insert(4)
bst.insert(6)
bst.insert(8)

print("Inorder Traversal:")
bst.inorder_traversal()
print("\nPreorder Traversal:")
bst.preorder_traversal()
print("\nPostorder Traversal:")
bst.postorder_traversal()

print("\nContains 4:", bst.contains(4))
print("Contains 9:", bst.contains(9))

bst.delete(5)
print("\nInorder Traversal after deleting 5:")
bst.inorder_traversal()
print()
# print(bst.is_bst_check())

root = TreeNode1(4)
root.left = TreeNode1(2)
root.right = TreeNode1(6)
root.left.left = TreeNode1(1)
root.left.right = TreeNode1(3)
root.right.left = TreeNode1(5)
root.right.right = TreeNode1(9)

is_valid_bst = bst.is_bst(root)
print(is_valid_bst)
