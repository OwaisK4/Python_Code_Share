class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_begin(self, data):
        node = Node(data)
        if self.head is None:
            self.head = node
        else:
            node.next = self.head
            self.head = node

    def print(self):
        node = self.head
        while node is not None:
            print(node.data, end=" ")
            node = node.next


l = LinkedList()
l.insert_begin(0)
l.insert_begin(1)
l.insert_begin(2)
l.print()
