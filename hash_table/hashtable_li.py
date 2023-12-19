class HashTable:
    def __init__(self, size):
        self.size = size
        self.keys = [None] * size
        self.values = [None] * size

    def hash(self, key):
        return hash(key) % self.size

    def put(self, key, value):
        index = self.hash(key)
        while self.keys[index] is not None and self.keys[index] != key:
            index = (index + 1) % self.size
        self.keys[index] = key
        self.values[index] = value

    def get(self, key):
        index = self.hash(key)
        while self.keys[index] is not None:
            if self.keys[index] == key:
                return self.values[index]
            index = (index + 1) % self.size
        raise KeyError(key)

    def display(self):
        for i in range(self.size):
            print(f"{i}: {self.keys[i]}={self.values[i]}")



table = HashTable(5)
table.put("apple", 1)
table.put("banana", 2)
table.put("cherry", 3)
table.put("date", 4)
table.put("elderberry", 5)
table.display()