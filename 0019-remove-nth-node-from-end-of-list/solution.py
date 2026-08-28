# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
       

        x=0
        curr=head
        while curr:
            x+=1
            curr=curr.next

        x-=n

        curr=head
        prev=None
        for _ in range(x):
            prev=curr
            curr=curr.next
            
        if prev:
            prev.next=curr.next
        else:
            head=head.next

        return head
            
