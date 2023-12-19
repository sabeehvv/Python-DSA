class Node:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

class Tree:
    def __init__(self):
        self.root = None

    def insert(self,data):
        if self.root is None:
            self.root = Node(data)
        else:
            self.insert_helper(self.root,data)


    def insert_helper(self,node,data):
        if node.data > data:
            if node.left is None:
                node.left = Node(data)
            else:
                self.insert_helper(node.left,data)
        else:
            if node.right is None:
                node.right = Node(data)
            else:
                self.insert_helper(node.right,data)


    def in_order_sorting(self):
        self.in_order_rec(self.root)


    def in_order_rec(self,node):
        if node is not None:
            self.in_order_rec(node.left)
            print(node.data)
            self.in_order_rec(node.right)

    def pre_order(self):
        self.pre_order_func(self.root)


    def pre_order_func(self,node):
        if node is not None:
            print(node.data)
            self.pre_order_func(node.left)
            self.pre_order_func(node.right)

    def post_orde(self):
        self.post_oreder_func(self.root)

    def post_oreder_func(self,node):
        if node is not None:
            self.post_oreder_func(node.left)
            self.post_oreder_func(node.right)
            print(node.data)

    def delete_main(self,data):
        self.root = self.delete_func(self.root,data)


    def delete_func(self,node,data):
        if node is None:
            return node
        if node.data > data:
            node.left = self.delete_func(node.left,data)
        elif node.data < data:
            node.right = self.delete_func(node.right,data)
        else:
            if node.left is None:
                temp = node.right
                node =None
                return temp
            elif node.right is None:
                temp = node.left
                node = None
                return temp
            else:
                temp = self.minimum_program(node.right)
                node.data = temp.data
                node.right = self.delete_func(node.right,temp.data)
        return node
    
    def minimum_program(self,node):
        current = node
        while current.left is not None:
            current = current.left
        return current




test = Tree()

test.insert(4)
test.insert(5)
test.insert(44)
test.insert(43)
test.insert(46)

print("pre")
test.pre_order()
print("in")
test.in_order_sorting()
test.delete_main(43)
print("post")
test.post_orde()