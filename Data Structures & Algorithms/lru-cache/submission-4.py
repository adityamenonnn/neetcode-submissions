class Node:
    def __init__(self,key,value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self,capacity):
        self.cache = {}
        self.capacity = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next, self.right.prev = self.right,self.left

    
    def remove(self,node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev
    
    def add(self,node):
        prev = self.right.prev
        prev.next = node
        node.next = self.right
        node.prev = prev
        self.right.prev = node
    
    def get(self,key):
        if key in self.cache:
            self.remove(self.cache[key])
            self.add(self.cache[key])
            return self.cache[key].value
        return -1

    def put(self,key,value):
        if key in self.cache:
            self.remove(self.cache[key])
            new = Node(key,value)
            self.cache[key]=new
            self.add(new)
        else:
            new = Node(key,value)
            self.cache[key]=new
            self.add(new)
        if len(self.cache)>self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        