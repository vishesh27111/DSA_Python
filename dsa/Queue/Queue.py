class Queue:
    def __init__(self, size):
        self.size = size
        self.front = self.rear = -1
        self.queue = [None]*size

    def enqueue(self, num):
        if self.rear >= (self.size-1):
            print("Queue is full")
            return

        self.rear+=1
        self.queue[self.rear] = num

        return

    def dequeue(self):
        if self.rear == -1:
            print("Queue is empty")
            return

        for i in range(self.rear):
            self.queue[i] = self.queue[i+1]

        self.queue[self.rear] = None
        self.rear-=1

        return