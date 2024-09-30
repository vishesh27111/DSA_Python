class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue_Using_LinkedList:
    def __init__(self):
        self.head = None
        self.rear = None

    def enqueue(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = self.rear = new_node
            return

        self.rear.next = new_node
        self.rear = new_node

        return

    def dequeue(self):

        if self.head is None:
            print("Queue is empty")
            return

        self.head = self.head.next

        return

    def peek(self):
        if self.head is None:
            print("Queue is Empty")
            return

        return self.head.data

    def PrintQueue(self):
        if self.head is None:
            print("Queue empty")
            return

        curr = self.head
        while curr is not None:
            print(curr.data, end = " ")
            curr = curr.next

        return