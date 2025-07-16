# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:

        store= []

        while head:
            store.append(head.val)
            head= head.next
        
        l=0
        r=len(store)-1

        while l<r:
            if store[l]!=store[r]:
                return False
            
            l+=1
            r-=1
            
        return True

    #time complexity O(n+n/2)=O(n)
    #space complexity O(n)
        