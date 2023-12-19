class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Que:
    def __init__(self):
        self.head = None
        self.tail = None

    def enqueu(self,data):
        new_node = Node(data)
        if self.tail is None:
            self.head = new_node
            self.tail = new_node
        self.tail.next = new_node
        self.tail = new_node
        
    def deque(self):
        if self.tail is None:
            print("empty")
        else:
            self.head = self.head.next


    def display(self):
        if self.head is None:
            print("empty")
        else:
            current_node = self.head
            while current_node is not None:
                print(f"{current_node.data}",end=" ")
                current_node = current_node.next

q = Que()
q.enqueu(4)
q.enqueu(6)
q.enqueu(8)
q.enqueu(4)
q.deque()
q.display()

