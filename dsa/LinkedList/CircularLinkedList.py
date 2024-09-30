class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class CircularLinkedList:
    def __init__(self):
        self.head = None

    def PrintCLL(self):
        if self.head is None:
            print("No elements in Linked List")
            return
        curr = self.head
        while curr.next is not self.head:
            print(curr.data, end=" ")
            curr = curr.next
        print(curr.data)

        return

    def Length(self):
        if self.head is None:
            return 0

        curr = self.head
        count = 0
        while curr.next is not self.head:
            curr = curr.next
            count+=1

        return count + 1

    def Insert_End(self, num):
        new_node = Node(num)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return

        curr = self.head
        while curr.next is not self.head:
            curr = curr.next

        curr.next = new_node
        new_node.next = self.head

        return

    def Insert_Start(self, num):
        new_node = Node(num)
        if self.head is None:
            self.head = new_node
            new_node.next = new_node
            return

        # new_node.next = self.head
        curr = self.head
        while curr.next is not self.head:
            curr = curr.next

        curr.next = new_node
        new_node.next = self.head
        self.head = new_node
        return

    def Insert_Index(self, num, index):
        if index == 0:
            self.Insert_Start(num)
            return
        elif index == self.Length():
            self.Insert_End(num)
        elif index > self.Length():
            print("Index out of range")
        else:
            new_node = Node(num)
            curr,prev = self.head, None
            i = 0
            while i < index:
                prev = curr
                curr = curr.next

            prev.next = new_node
            new_node.next = curr

        return