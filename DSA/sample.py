class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class linked_list:
    def __init__(self):
        self.head = None
    def add_node(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
            new_node.prev = current_node


    def delete_node(self,x):
        if self.head is None:
            return
        if self.head.data == x:
            self.head = self.head.next
        else:
            current_node = self.head
            while current_node.next is not None:
                if current_node.data == x:
                    current_node = current_node.next
                    return
                current_node = current_node.next




    def display(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            current_node = self.head
            while current_node.next is not None:
                print(current_node,end="")
                current_node = current_node.next

    
        