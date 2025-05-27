class ListNode:
    def __init__(self,key=-1,value=-1, next=None):
        self.key=key
        self.val=value
        self.next= next


class MyHashMap:

    def __init__(self):
        self.hash=[ListNode() for i in range (1000)]

    def put(self, key: int, value: int) -> None:
        index= key % len(self.hash)
        cur=self.hash[index]

        while cur.next:
            if cur.next.key==key:
                cur.next.val= value
                return
            cur=cur.next
        
        cur.next=ListNode(key,value)
    
    def get(self, key: int) -> int:
        index= key % len(self.hash)
        cur=self.hash[index]
    
        while cur:
            if cur.key==key:
                return cur.val
            cur=cur.next

        return -1


    def remove(self, key: int) -> None:
        index= key % len(self.hash)
        cur=self.hash[index]

        while cur and cur.next:
            if cur.next.key== key: #if its the key we want to remove
                cur.next= cur.next.next
                return
            cur=cur.next

#time complexity O(1)
#space complexity O(N)   


# Your MyHashMap object will be instantiated and called as such:
# obj = MyHashMap()
# obj.put(key,value)
# param_2 = obj.get(key)
# obj.remove(key)