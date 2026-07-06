# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> List[List[int]]:
        if not root:return []
        
        s=[(root,[],0)]
        res=[]
        while s:
            n,path,total=s.pop()
            path=path.copy()
            path.append(n.val)
            total+=n.val
            # if total>targetSum:
            #     continue
            if not n.left and not n.right:
                if total==targetSum:
                    res.append(path)
                continue
            if n.left:
                s.append((n.left,path,total))
            if n.right:
                s.append((n.right,path,total))

        return res
