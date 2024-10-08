class MinHeap:
    def __init__(self):
        self.heap = []

    def parent(self,index):
        return (index-1)//2
    def l_child(self,index):
        return 2*index+1
    def r_child(self,index):
        return 2*index+2

    def insert(self,value):
        self.heap.append(value)
        self.heapify_up(len(self.heap) - 1)

    def heapify_up(self, index):
        parent_index = self.parent(index)

        while index > 0 and self.heap[index] > self.heap[parent_index]:
            self.heap[index], self.heap[parent_index] = self.heap[parent_index], self.heap[index]
            index = parent_index

    def heapify_down(self, index):

        smallest = index
        l_index = self.l_child(index)
        r_index = self.r_child(index)

        if l_index < len(self.heap) and self.heap[l_index] < self.heap[smallest]:
            smallest = l_index
        if r_index < len(self.heap) and self.heap[r_index] < self.heap[smallest]:
            smallest = r_index

        if smallest != index:
            self.heap[index], self.heap[smallest] = self.heap[smallest], self.heap[index]
            self.heapify_down(smallest)

    def extract_min(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()

        root = self.heap[0]

        self.heap[0] = self.heap.pop()

        self.heapify_down(0)
        return root