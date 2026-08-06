"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Optional[Node]') -> 'Optional[Node]':
        if not root:return None

        q=deque([root])

        while q:
            to=None
            for _ in range(len(q)):
                n=q.popleft()
                n.next=to
                to=n

                if n.right:q.append(n.right)
                if n.left:q.append(n.left)

        return root
