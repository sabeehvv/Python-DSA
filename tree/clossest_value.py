class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


def find_closest_value(root, target):
    closest = float('inf')
    return _find_closest_value_helper(root, target, closest)


def _find_closest_value_helper(node, target, closest):
    if node is None:
        return closest

    if node.data == target:
        return node.data

    if abs(node.data - target) < abs(closest - target):
        closest = node.data

    if target < node.data:
        return _find_closest_value_helper(node.left, target, closest)
    else:
        return _find_closest_value_helper(node.right, target, closest)



root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(5)
root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

target = 3.7
closest_value = find_closest_value(root, target)
print("Closest value to", target, "in the tree:", closest_value)
