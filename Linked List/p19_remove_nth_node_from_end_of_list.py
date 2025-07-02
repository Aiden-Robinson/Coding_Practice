# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        #dummy node

        dummy = ListNode(0,head)

        left= dummy
        right= head

        while n>0 and right: #get right ahead by this amount
            right= right.next
            n-=1
        
        while right: #push it to the end
            right = right.next
            left= left.next
        
        #make the deletion
        left.next= left.next.next

        return dummy.next

#time complexity O(N)
#space complexity O(1)