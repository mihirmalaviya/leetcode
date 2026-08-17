# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        temp=ListNode()
        temp.next=head

        prev=temp
        curr=head

        while curr:
            dup=False
            while curr.next and curr.next.val==curr.val:
                curr=curr.next
                dup=True
            
            if dup:
                prev.next=curr.next
            else:
                prev=prev.next
                
            curr=curr.next

        return temp.next
