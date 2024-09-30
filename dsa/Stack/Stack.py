class Stack:
    def __init__(self, capacity):
        self.capacity = capacity
        self.top = -1
        self.stack = [None]*capacity

    def push(self, data):
        if self.top >= (self.capacity-1):
            print("Stack is full")
            return

        self.top+=1
        self.stack[self.top] = data

        return

    def pop(self):
        if self.top == -1:
            print("Stack is empty")

        popped = self.stack[self.top]
        self.top-=1;

        return popped

    def peek(self):
        return self.stack[self.top] if self.top>-1 else "Stack is empty"
