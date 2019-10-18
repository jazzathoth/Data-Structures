from doubly_linked_list import DoublyLinkedList, ListNode


class LCacheNode(ListNode):
    def __init__(self, key, value, prev=None, next=None):
        super().__init__(value, prev, next)
        self.key = key


class LRUCache:
    """
    Our LRUCache class keeps track of the max number of nodes it
    can hold, the current number of nodes it is holding, a doubly-
    linked list that holds the key-value entries in the correct
    order, as well as a storage dict that provides fast access
    to every node stored in the cache.
    """
    def __init__(self, limit=10):
        self.limit = limit
        self.dict_store = {}
        self.ll_store = DoublyLinkedList()
        self.size = 0
        return

    """
    Retrieves the value associated with the given key. Also
    needs to move the key-value pair to the end of the order
    such that the pair is considered most-recently used.
    Returns the value associated with the key or None if the
    key-value pair doesn't exist in the cache.
    """
    def get(self, key):
        if key in self.dict_store:
            self.ll_store.move_to_end(self.dict_store[key])
            return self.dict_store[key].value
        else:
            return


    """
    Adds the given key-value pair to the cache. The newly-
    added pair should be considered the most-recently used
    entry in the cache. If the cache is already at max capacity
    before this entry is added, then the oldest entry in the
    cache needs to be removed to make room. Additionally, in the
    case that the key already exists in the cache, we simply
    want to overwrite the old value associated with the key with
    the newly-specified value.
    """
    def set(self, key, value):
        if key in self.dict_store:
            self.ll_store.move_to_end(self.dict_store[key])
            self.ll_store.tail.value = value
        else:
            if self.size >= self.limit:
                removed_key = self.ll_store.head.key
                self.ll_store.remove_from_head()
                self.dict_store.pop(removed_key)
                self.size += -1

            node = LCacheNode(key, value)
            self.ll_store.add_to_tail(node)
            self.dict_store[key] = node
            self.size += 1
        return
