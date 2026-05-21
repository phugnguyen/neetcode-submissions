class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value

        self.prev, self.nxt = None, None

class LRUCache:

    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}

        # LRU on left, MRU on right on doubly linked list
        self.LRU, self.MRU = Node(-1,-1), Node(-1,-1)
        self.LRU.nxt = self.MRU
        self.MRU.prev = self.LRU

    # insert to the right as this node will now be MRU
    def insert(self, node):
        prev, nxt = self.MRU.prev, self.MRU

        prev.nxt = node
        node.nxt = nxt
        node.prev = prev
        self.MRU.prev = node
    
    def remove(self, node):
        prev, nxt = node.prev, node.nxt

        prev.nxt = nxt
        nxt.prev = prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            node = Node(key, value)
            self.remove(self.cache[key])
            self.cache[key] = node
            self.insert(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.insert(node)

            if len(self.cache) > self.cap:
                curr = self.LRU.nxt
                self.remove(curr)
                del self.cache[curr.key]
