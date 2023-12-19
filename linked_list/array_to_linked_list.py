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


def array_to_linked_list(arr):
    linked_list = LinkedList()
    for element in arr:
        linked_list.add_node(element)
    return linked_list


arr = [1, 2, 3, 4, 5]
linked_list = array_to_linked_list(arr)
