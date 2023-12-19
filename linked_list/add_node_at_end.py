# class Node:
#     def __init__(self, data):
#         self.data = data
#         self.next = None


# class LinkedList:
#     def __init__(self):
#         self.head = None

#     def add_node(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current_node = self.head
#             while current_node.next is not None:
#                 current_node = current_node.next
#             current_node.next = new_node

#     def add_node_at_end(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             current_node = self.head
#             while current_node.next is not None:
#                 current_node = current_node.next
#             current_node.next = new_node

#     def add_node_at_beginning(self, data):
#         new_node = Node(data)
#         if self.head is None:
#             self.head = new_node
#         else:
#             new_node.next = self.head
#             self.head = new_node

#     def display(self):
#         if self.head is None:
#             print("Linked list is empty")
#         else:
#             current_node = self.head
#             while current_node is not None:
#                 print(current_node.data, end=" ")
#                 current_node = current_node.next


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def add_node(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = newnode

    def add_node_at_end(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = newnode

    def add_node_at_beginning(self, data):
        newnode = Node(data)
        if self.head is None:
            self.head = newnode
        else:
            newnode.next = self.head
            self.head = newnode

    def delete_node(self,value):
        if self.head is None:
            return
        elif self.head.data == value:
            self.head = self.head.next
            return
        else:
            current_node = self.head
            while current_node.next is not None:
                if current_node.next.data == value:
                    current_node.next = current_node.next.next
                    return
                current_node = current_node.next

    def display(self):
        if self.head is None:
            print("It's Empty")
        else:
            current_node = self.head
            while current_node is not None:
                print(current_node.data, end=" ")
                current_node = current_node.next
            


linked_list = LinkedList()
linked_list.add_node(1)
linked_list.add_node(2)


linked_list.add_node_at_end(3)


linked_list.add_node_at_beginning(0)

linked_list.delete_node(0)


linked_list.display()
