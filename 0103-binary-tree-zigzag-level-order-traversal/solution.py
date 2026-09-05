# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        
        q=deque([root])
        res=[]
        i=0
        while q:
            res.append([])
            for _ in range(len(q)):
                n=q.popleft()
                res[-1].append(n.val)
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
            if i%2:
                res[-1].reverse()
            i+=1
        

        
        return res

