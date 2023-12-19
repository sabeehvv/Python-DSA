class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [None] * size

    def hash(self, key):
        return hash(key) % self.size


    def put(self, key, value):
        index = self.hash(key)
        if self.table[index] is None:
            self.table[index] = Node(key, value)
        else:
            node = self.table[index]
            while node.next is not None and node.key != key:
                node = node.next
            if node.key == key:
                node.value = value
            else:
                node.next = Node(key, value)

    def get(self, key):
        index = self.hash(key)
        node = self.table[index]
        while node is not None:
            if node.key == key:
                return node.value
            node = node.next
        raise KeyError(key)

    def delete(self, key):
        index = self.hash(key)
        node = self.table[index]
        # prev = None
        while node is not None:
            if node.key == key:
                # if prev is None:
                self.table[index] = node.next
                # else:
                #     prev.next = node.next
                return
            # prev = node
            node = node.next
        raise KeyError(key)

    def display(self):
        for i in range(self.size):
            print(f"{i}:", end=" ")
            node = self.table[i]
            while node is not None:
                print(f"{node.key}={node.value}", end=" -> ")
                node = node.next
            print("None")



table = HashTable(5)
table.put("apple", 1)
table.put("banana", 2)
table.put("cherry", 3)
table.put("date", 4)
table.put("elderberry", 5)
table.put("fig", 6)
table.put("apple", 66)
table.display()
# table.delete("apple")
# table.put("grape", 100)
# table.display()