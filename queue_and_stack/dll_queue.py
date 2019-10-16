
from doubly_linked_list import DoublyLinkedList


class QueueLambda:
    def __init__(self):
        self.size = 0
        self.storage = DoublyLinkedList()

    def __len__(self):
        return len(self.storage)

    def enqueue(self, value):
        self.storage.add_to_tail(value)
        return

    def dequeue(self):
        if self.__len__() == 0:
            return
        else:
            value = self.storage.head.value
            self.storage.remove_from_head()
            return value

    def len(self):
        return len(self.storage)
