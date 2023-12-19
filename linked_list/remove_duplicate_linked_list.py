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

    # def remove_duplicates(self):
    #     if self.head is None:
    #         print("Linked list is Empty")
    #     current_node = self.head
    #     while current_node is not None:
    #         new_node = current_node
    #         while new_node.next is not None:
    #             if current_node.data == new_node.next.data:
    #                 new_node.next = new_node.next.next
    #             else:
    #                 new_node = new_node.next
    #         current_node = current_node.next

    def print_linked_list(self):
        if self.head is None:
            print("Linked list is empty")
            return
        current_node = self.head
        elements = []
        while current_node is not None:
            elements.append(current_node.data)
            current_node = current_node.next
        print("Linked list:", elements)


    def remove_duplicates(self):
        if self.head is None:
            print("Empty")
            return
        current_node = self.head
        while current_node.next is not None:
            new_node = current_node
            while new_node.next is not None:
                if current_node.data == new_node.next.data:
                    new_node.next = new_node.next.next




linked_list = LinkedList()
linked_list.add_node(1)
linked_list.add_node(1)
linked_list.add_node(2)
linked_list.add_node(3)
linked_list.add_node(3)
linked_list.add_node(3)
linked_list.add_node(1)


linked_list.print_linked_list() 


linked_list.remove_duplicates()


linked_list.print_linked_list()  