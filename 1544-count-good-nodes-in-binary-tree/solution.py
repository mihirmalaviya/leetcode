# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        res=0
        s=[(root,root.val)]
        while s:
            n,x=s.pop()
            if n.val>=x:
                res+=1
                x=n.val
            if n.left:s.append((n.left,x))
            if n.right:s.append((n.right,x))
        return res
 
