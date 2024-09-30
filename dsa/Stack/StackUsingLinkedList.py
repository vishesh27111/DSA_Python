class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack_Using_LinkedList:

    def __init__(self):
        self.head = None

    def push(self, data):
        new_node = Node(data)

        new_node.next = self.head
        self.head = new_node
        return

    def pop(self):
        if self.head is None:
            print("No elements in stack")
            return

        popped = self.head
        self.head = self.head.next

        return popped.data

    def peek(self):
        print("Stack is empty") if self.head is None else self.head.data

    def PrintStack(self):
        if self.head is None:
            print("Stack is empty")
            return

        curr = self.head
        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next

        return