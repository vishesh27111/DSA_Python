class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def PrintLinkedList(self):
        if self.head == None:
            print("No elements in Linked List")
            return

        curr = self.head
        while curr is not None:
            print(curr.data, end="->")
            curr = curr.next

        print("\n")
        return

    def Length(self):
        if self.head == None:
            return 0

        count = 0
        curr = self.head
        while curr is not None:
            count+=1
            curr = curr.next

        return count

    # Insert at end
    def insert(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        curr = self.head
        while curr.next is not None:
            curr = curr.next

        curr.next = new_node

        return

    # Insert at index
    def insert_at_index(self, data, index):
        new_node = Node(data)

        if index > self.Length():
            print("Index out of range")

        if index == 0:
            new_node.next = self.head
            self.head = new_node
            return

        curr, prev = self.head, None
        i=0
        while i<index:
            prev = curr
            curr = curr.next
            i+=1
        prev.next = new_node
        new_node.next = curr

        return

    def deleteKey(self, data):
        if self.head == None:
            print("No elements in linked list")

        if self.head.data == data:
            self.head = self.head.next
            return

        curr,prev = self.head, None

        while curr is not None:
            if curr.data == data:
                prev.next = curr.next
                return
            prev = curr
            curr= curr.next

        print("Element not found")
        return

    def deletePosition(self, index):
        if index >= (self.Length()-1):
            print("Index out of range")
            return

        if index == 0:
            self.head = self.head.next
            return

        curr, prev = self.head, None
        i=0
        while i<index:
            prev = curr
            curr = curr.next
            i+=1

        prev.next = curr.next
        return