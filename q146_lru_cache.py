from collections import OrderedDict

class LRUCache:
    def __init__(self, capacity: int):
        self.cache = OrderedDict()
        self.capacity = capacity

    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.cache.move_to_end(key, last=False)
        return self.cache[key]

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key] = value
            return
        if len(self.cache) == self.capacity:
            self.cache.popitem()
        self.cache[key] = value
        self.cache.move_to_end(key)

class Node:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, cap):
        self.cache = {}
        self.sentinal = Node(0, 0)
        self.sentinal.prev = self.sentinal
        self.sentinal.next = self.sentinal
        self.cap = cap
        
    def _move_to_start(self, node):
        if node.prev:
            node.prev.next = node.next
            node.next.prev = node.prev
        prev = self.sentinal
        node.next = prev.next
        node.next.prev = node
        prev.next = node
        node.prev = prev

    def get(self, key):
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self._move_to_start(node)
        return node.val
    
    def put(self, key, val):
        if key in self.cache:
            node = self.cache[key]
            node.val = val
        elif len(self.cache) == self.cap:
            node = self.sentinal.prev
            self.cache.pop(node.key)
            node.key = key
            node.val = val
        else:
            node = Node(key, val)
        self.cache[key] = node
        self._move_to_start(node)
        

if __name__ == '__main__':
    cache = LRUCache(2)
    cache.put(1, 1)
    cache.put(2, 2)
    cache.get(1)
    cache.put(3, 3)
    cache.get(2)
    cache.put(4, 4)
    cache.get(1)
    cache.get(3)
    cache.get(4)