# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        heap=[]
        for i in range(len(lists)):
            l=lists[i]
            if l:
                heappush(heap,(l.val,i,l))
            else:
                pass

        if not heap: return None

        root=ListNode()
        curr=root
        while heap:
            val,i,node=heappop(heap)

            curr.next=node
            curr=curr.next

            if node.next:
                heappush(heap, (node.next.val, i,node.next))
            
        return root.next
            
            


