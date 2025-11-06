# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head:
            return head
        
        dummy= ListNode(0,head)
        prev= dummy
        cur=head
    
        while cur and cur.next:
            #define
            nxt= cur.next

            #swap
            cur.next= nxt.next
            nxt.next=cur
            prev.next= nxt

            #iterate
            prev=cur
            cur=cur.next
        return dummy.next

#time complexity O(N)
#space complexity O(1)