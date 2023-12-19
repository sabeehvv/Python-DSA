class Node:
    def __init__(self,data) -> None:
        self.data = data
        self.next = None

class linkedlist:
    def __init__(self) -> None:
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

    def delete(self,value):
        if self.head is None:
            return
        current_node = self.head
        while current_node.next is not None:
            if current_node.data == value:
                current_node = current_node.next
                return
            current_node = current_node.next

    def insert_before(self,value,x):
        if self.head is None:
            return
        if self.head.data == x:
            new_node = Node(value)
            new_node.next = self.head
            self.head = new_node
            return
        current_node = self.head
        while current_node.next is not None:
            if current_node.data == x:
                new_node = Node(value)
                new_node.next = current_node
                current_node = new_node
                return
            current_node = current_node.next

    def insert_after(self,value,x):
        if self.head is None:
            return
        current_node = self.head
        while current_node.next is not None:
            if current_node.data == x:
                new_node = Node(value)
                new_node.next = current_node.next
                current_node.next = new_node
                return
            current_node = current_node.next

    def display(self):
        if self.head is None:
            print("Linked list Empty")
        else:
            current_node = self.head
            while current_node.next is not None:
                print(current_node.data , end="")
                current_node = current_node.next
    

    def binary_search(arr, data):
        low = 0
        high = len(arr)-1
        while low <= high:
            mid = (low+high)//2
            if arr[mid]==data:
                return mid
            elif arr[mid]<data:
                low = mid +1
            else:
                high = mid -1
        return -1
    
