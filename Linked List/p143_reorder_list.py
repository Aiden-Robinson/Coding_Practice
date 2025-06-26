# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        #find the midpoint of the linked list

        slow=head
        fast= head.next

        while fast and fast.next:
            slow=slow.next
            fast=fast.next.next

        #reverse the second half of the list

        second = slow.next #where the second half starts
        slow.next= None
        prev=None

        while second: #reversing the second portion of the list
            temp= second.next
            second.next= prev
            prev= second
            second= temp

        #merge the two halfs

        second = prev #declare list 1
        first= head #declare list 2

        while second: #because second is the shorter of the lists
            temp1= first.next
            temp2= second.next
            first.next= second
            second.next=temp1
            first= temp1
            second=temp2
#time complexity O(N)
#space complexity O(1)
        

        