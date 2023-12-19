class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class queue:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueue(self,data):
        new_node = Node(data)

        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        self.tail = new_node

    def dequeue(self):
        if self.head is None:
            print("Empty")
        data = self.head.data
        self.head = self.head.next
        if self.head is None:
            self.tail = None
        return data
    
    def display(self):
        if self.head is None:
            print("empty")
            return
        current_node = self.head
        while current_node.next is not None:
            print(current_node.data , end=" ")
            current_node = current_node.next






q = queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
q.display()  
q.dequeue()
print("\n")
q.display()  

q.dequeue()
q.dequeue()
print("\n")
q.display()


