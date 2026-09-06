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
        
        slow=fast=head
        while fast and fast.next:
            fast=fast.next.next
            slow=slow.next

        second=slow.next
        slow.next=None

        curr=second
        prev=None
        while curr:
            temp=curr.next
            curr.next=prev
            prev=curr
            curr=temp
        
        a=head
        b=prev
        while a and b:
            an=a.next
            bn=b.next

            a.next=b
            b.next=an

            a=an
            b=bn
