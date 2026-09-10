class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.cache = {} #stores the value:Node pointer 
        self.capacity = capacity

        #towards the left, is least recently used i.e LRU right is most recetly used
        self.left = Node(0,0)
        self.right = Node(0,0)
        
        #connecting
        self.left.next, self.right.prev = self.right,self.left

    
    def remove(self,node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev 
    
    def add(self,node):
        #adding to the right most side
        prev = self.right.prev
        prev.next = node
        node.prev = prev 
        self.right.prev = node
        node.next = self.right


    def get(self, key: int) -> int:
        #if its get-ed then we need to move it to most recently used, by removing the node and adding to the right most
        if key in self.cache:
            #remove the node,add it to the right
            self.remove(self.cache[key])
            self.add(self.cache[key])
            #returning value
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        new = Node(key,value)
        self.cache[key]=new
        self.add(new)

        if len(self.cache)>self.capacity:
            lru = self.left.next 
            self.remove(lru)
            del self.cache[lru.key]
