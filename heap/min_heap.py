class MinHeap:
    def __init__(self):
        self.heap = []

    def insert(self, item):
        self.heap.append(item)
        self._heapify_up(len(self.heap) - 1)

    def extract_min(self):
        if not self.heap:
            return None
        self._swap(0, len(self.heap) - 1)
        minimum = self.heap.pop()
        self._heapify_down(0)
        return minimum

    def _heapify_up(self, index):
        parent_index = (index - 1) // 2
        if parent_index >= 0 and self.heap[index] < self.heap[parent_index]:
            self._swap(index, parent_index)
            self._heapify_up(parent_index)

    def _heapify_down(self, index):
        left_child_index = 2 * index + 1
        right_child_index = 2 * index + 2
        smallest = index

        if (
            left_child_index < len(self.heap)
            and self.heap[left_child_index] < self.heap[smallest]
        ):
            smallest = left_child_index

        if (
            right_child_index < len(self.heap)
            and self.heap[right_child_index] < self.heap[smallest]
        ):
            smallest = right_child_index

        if smallest != index:
            self._swap(index, smallest)
            self._heapify_down(smallest)

    def _swap(self, i, j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]