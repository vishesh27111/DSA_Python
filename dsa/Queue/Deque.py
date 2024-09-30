class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        self.prev = None

class Deque:
    def __init__(self):
        self.front = None
        self.rear = None

    def insert_front(self, num):
        new_node = Node(num)

        if self.front == None:
            self.front = self.rear = new_node

        else:
            new_node.next = self.front
            self.front.prev = new_node
            self.front = new_node
        return

    def insert_rear(self, num):
        new_node = Node(num)

        if self.rear is None:
            self.front = self.rear = new_node

        else:
            self.rear.next = new_node
            new_node.prev = self.rear
            self.rear = new_node

        return

    def delete_front(self):
        if self.front is None:
            print("Queue is empty")

        elif self.front.next is None:
            self.front = self.rear = None

        else:
            self.front = self.front.next
            self.front.prev = None

        return

    def delete_rear(self):
        if self.rear is None:
            print("Queue is empty")

        elif self.rear.prev is None:
            self.front = self.rear = None

        else:
            self.rear = self.rear.prev
            self.rear.next = None

        return

    def display(self):
        if self.front is None:
            print("Queue is empty")

        else:
            curr = self.front
            while curr is not None:
                print(curr.data, end=" ")
                curr = curr.next
            print()

        return
