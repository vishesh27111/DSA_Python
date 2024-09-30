class CircularQueue:
    def __init__(self, size):
        self.size = size
        self.queue = [None] * size
        self.front = self.rear = -1

    def enqueue(self, num):

        if self.front == -1:
            self.front += 1
            self.rear += 1
            self.queue[self.rear] = num

        elif (self.rear+1)%self.size == self.front:
            print("Queue is full")

        else:
            self.rear = (self.rear + 1) % self.size
            self.queue[self.rear] = num
        return

    def dequeue(self):

        if self.front == -1:
            print("Queue is empty")
        elif self.front == self.rear:
            self.front = self.rear = -1
        else:
            popped = self.queue[self.front]
            self.front = (self.front+1)%self.size

        return

    def display(self):

        if self.front == -1:
            print("Queue is empty")

        elif self.rear>=self.front:

            for i in range(self.front, self.rear + 1):
                print(self.queue[i],end = " ")
            print()

        else:

            for i in range(self.front, self.size):
                print(self.queue[i], end = " ")
            for i in (0, self.rear + 1):
                print(self.queue[i],end = " ")
            print()