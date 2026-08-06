# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        
        curr=float('-inf')

        def dfs(node):
            nonlocal curr

            if not node:
                return True
            
            if not dfs(node.left):
                return False

            if not node.val>curr:
                return False
            curr=node.val

            return dfs(node.right)
        
        return dfs(root)

