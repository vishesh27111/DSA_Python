from types import new_class


class Node:
    def __init__(self, data):
        self.prev = None
        self.data = data
        self.next = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None

    def Insert_at_End(self, num):
        new_node = Node(num)
        if self.head is None:
            self.head = new_node
            return

        curr = self.head
        while curr.next is not None:
            curr = curr.next

        curr.next = new_node
        new_node.prev = curr

        return

    def Insert_at_Begin(self, num):
        new_node = Node(num)
        if self.head is None:
            self.head = new_node
            return

        new_node.next = self.head
        self.head.prev = new_node

        self.head = new_node

        return

    def Insert_at_Index(self, num, index):
        if index == 0:
            self.Insert_at_Begin(num)
        elif index == self.Length():
            self.Insert_at_End(num)
        elif index > self.Length():
            print("Index out of range")
        else:
            new_node = Node(num)
            curr,pre = self.head, None
            i = 0
            while i < index:
                prev = curr
                curr = curr.next

            pre.next = new_node
            new_node.prev = pre
            new_node.next = curr
            curr.prev = new_node

        return

    def TraverseForward(self):
        if self.head is None:
            print("No elements in Linked List")
            return

        curr = self.head

        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.next
        print("\n")
        return

    def TraverseBackward(self):
        curr = self.head

        while curr.next is not None:
            curr = curr.next

        while curr is not None:
            print(curr.data, end=" ")
            curr = curr.prev

        return

    def Length(self):
        if self.head is None:
            return 0
        curr = self.head
        count = 0
        while curr is not None:
            count+=1
            curr = curr.next

        return count

    def RemoveKey(self, key):
        curr,pre = self.head, None
        if curr is None:
            return
        if curr.data == key:
            self.RemoveFirst()
            return

        while curr is not None:
            if curr.data == key:
                if curr.next is None:
                    pre.next = None
                else:
                    pre.next = curr.next
                    curr.next.prev = pre

                print("Element removed")
                return

            pre = curr
            curr = curr.next

        print("Element not found")
        return

    def RemoveFirst(self):
        if self.head is None:
            return

        self.head = self.head.next
        self.head.prev = None
        return