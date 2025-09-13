class Node:
    def __init__(self,key,val):
        self.key=key
        self.val=val
        self.prev, self.next= None, None
class LRUCache:

    def __init__(self, capacity: int):
        self.capacity=capacity
        self.cache={}
        self.left, self.right= Node(0,0), Node(0,0)
        self.left.next= self.right #doubly link the left and right
        self.right.prev=self.left
        
    def remove(self,node):
        prev, nxt= node.prev, node.next
        prev.next= nxt
        nxt.prev= prev

    def insert(self,node): #insert at right most identifying it as most recently used 
        prev= self.right.prev
        nxt= self.right

        prev.next= node
        node.next=nxt
        nxt.prev=node
        node.prev=prev


    def get(self, key: int) -> int:
        if key in self.cache:
            self.remove(self.cache[key])
            self.insert(self.cache[key])
            return self.cache[key].val
        return -1
            
        

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key]) #delete old entry
        self.cache[key]=Node(key, value) #create the hasmap entry
        self.insert(self.cache[key]) #insert new entry into linked list 


        if len(self.cache) > self.capacity:
            lru= self.left.next
            self.remove(lru)
            del self.cache[lru.key]
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)