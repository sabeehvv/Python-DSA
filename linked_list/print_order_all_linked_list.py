class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node

    def print_in_order(self):
        if self.head is None:
            print("Linked list is empty")
            return
        current_node = self.head
        elements = []
        while current_node is not None:
            elements.append(current_node.data)
            current_node = current_node.next
        print("Linked list in order:", elements)

    def print_in_reverse_order(self):
        if self.head is None:
            print("Linked list is empty")
            return
        current_node = self.head
        elements = []
        while current_node is not None:
            elements.insert(0, current_node.data)
            current_node = current_node.next
        print("Linked list in reverse order:", elements)
        i = len(elements)-1
        while i >= 0:
            print(elements[i],end=' ')
            i -= 1



linked_list = LinkedList()
linked_list.add_node(1)
linked_list.add_node(2)
linked_list.add_node(3)


linked_list.print_in_order() 


linked_list.print_in_reverse_order()
