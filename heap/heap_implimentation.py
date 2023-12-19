class Heap:
    def __init__(self):
        self.heap = []

    def parent(self, i):
        return (i - 1) // 2

    def left_child(self, i):
        return 2 * i + 1

    def right_child(self, i):
        return 2 * i + 2

    def insert(self, value):
        self.heap.append(value)
        self._sift_up(len(self.heap) - 1)

    def extract_min(self):
        if self.is_empty():
            raise IndexError("Heap is empty")
        
        minimum = self.heap[0]
        last_element = self.heap.pop()
        if not self.is_empty():
            self.heap[0] = last_element
            self._sift_down(0)
        return minimum

    def is_empty(self):
        return len(self.heap) == 0

    def _sift_up(self, i):
        while i > 0 and self.heap[i] < self.heap[self.parent(i)]:
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)

    def _sift_down(self, i):
        min_index = i
        left = self.left_child(i)
        right = self.right_child(i)

        if left < len(self.heap) and self.heap[left] < self.heap[min_index]:
            min_index = left

        if right < len(self.heap) and self.heap[right] < self.heap[min_index]:
            min_index = right

        if i != min_index:
            self.heap[i], self.heap[min_index] = self.heap[min_index], self.heap[i]
            self._sift_down(min_index)



heap = Heap()

heap.insert(5)
heap.insert(3)
heap.insert(8)
heap.insert(1)
heap.insert(10)


minimum = heap.extract_min()
print("Minimum element:", minimum)


print("Is heap empty?", heap.is_empty()) 

minimum = heap.extract_min()
print("Minimum element:", minimum)


heap.insert(2)
heap.insert(6)


minimum = heap.extract_min()
print("Minimum element:", minimum)
