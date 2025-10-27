# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
       #leverage repeated cyclic nature of rotations, repeats after n rotations

        if not head:
            return head
        tail= head
        n=1

        while tail.next:
            
            tail=tail.next
            n+=1
        rotations= k%n

        if rotations==0:
            return head
        
        cur= head

        for i in range(n-rotations-1):
            cur=cur.next
        
        
        newHead= cur.next
        cur.next= None
        tail.next=head
        return newHead

#time complexity: O(n)
#space complexity: O(1)