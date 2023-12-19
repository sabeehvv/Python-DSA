class Queue:
    def __init__(self):
        self.items = []
        self.size = 0

    def is_empty(self):
        return self.items == 0
    
    def enqueue(self,data):
        self.items.append(data)
        self.size += 1

    def dequeue(self):
        if not self.is_empty():
            data = self.items[0]
            self.items = self.items[1:]
            self.size -= 1
            return data
        else:
            print("empty")

    def display(self):
        print(self.items)



q = Queue()

q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

q.display() 

print(q.dequeue())

q.display()