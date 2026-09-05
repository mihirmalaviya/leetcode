# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head:
            return
            
        dummy=ListNode(next=head)
        prev=dummy
        n=0
        while prev.next:
            prev=prev.next
            n+=1
        #prev.next must be none
        k%=n
        if k==0:
            return head
        
        prev.next = dummy.next

        prev=dummy

        for _ in range(n-k):
            prev=prev.next

        res=prev.next 
        prev.next=None

        return res

        


'''

take the last one and point it at the first one

snip the nth one

return the nth next one

'''
