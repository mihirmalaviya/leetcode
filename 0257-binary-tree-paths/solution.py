# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        

        res=[]
        curr=[]

        def dfs(n):
            if not n:
                return

            curr.append(str(n.val))

            if not n.left and not n.right:
                res.append("->".join(curr))
            else:
                dfs(n.left)
                dfs(n.right)

            curr.pop()

        dfs(root)
        return res
