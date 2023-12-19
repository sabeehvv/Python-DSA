class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None

    def push(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        

    def display(self):
        if self.head is None:
            print("Linked is Empty")
            return
        current_node = self.head
        while current_node.next is not None:
            print(current_node.data ,end=" ")
            current_node =current_node.next
            
        