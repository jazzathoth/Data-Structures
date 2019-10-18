class Node:
    def __init__(self, value ):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def add_to_head(self, node):
        node.next = self.head

    def reverse(self):

        current =
        prev = self.head

        while
