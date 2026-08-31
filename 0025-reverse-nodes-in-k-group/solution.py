# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if not head or not head.next or k==1:
            return head
        
        dummy=ListNode(0,head)
        before=dummy

        end=head
        curr=head
        while 1:
            i=0
            while i<k and end:
                end=end.next
                i+=1
            if i<k:
                break
            
            group_head=curr
            prev=None
            while curr!=end:
                temp=curr.next
                curr.next=prev
                prev=curr
                curr=temp
            
            before.next=prev
            group_head.next=end
            before=group_head
            
        return dummy.next

            
            
