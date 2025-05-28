# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: Optional[ListNode]) -> int:
        
       
        cur= head
        arr= []

        while cur:
            arr.append(cur.val)
            cur=cur.next
        
        total=0
        for index, val in enumerate (arr[::-1]): #reverse the array
            if val:
                total+=2**index

        return total

#time complexity O(N)
#Space complexity O(N)
        

