# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        
        res=None

        def dfs(n):
            nonlocal res
            if not n:
                return False

            if n==p or n==q:
                res=n
                return True

            l=dfs(n.left)
            r=dfs(n.right)
            
            if l and r:
                res=n
                return True 
            
            return l or r
            
        dfs(root)
        return res



                
