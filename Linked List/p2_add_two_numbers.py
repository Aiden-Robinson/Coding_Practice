# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        dummy= ListNode() #will be used to store result
        cur=dummy
        carry=0
        while l1 or l2 or carry:
            v1= l1.val if l1 else 0
            v2= l2.val if l2 else 0

            addition= v1+v2+carry

            toAdd= addition%10
            carry= addition//10

            cur.next=ListNode(toAdd)
            cur=cur.next
            l1=l1.next if l1 else None
            l2=l2.next if l2 else None
        return dummy.next

       
#time complexity O(max(N,M))
#space complexity O(max(N,M))


        