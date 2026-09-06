# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        n=len(preorder)
        root=TreeNode(val=preorder[0])
        prev=[root]

        j=0
        for i in range(1,n):
            x=TreeNode(val=preorder[i])
            if prev[-1].val != inorder[j]:
                prev[-1].left=x
            else:
                parent=None
                while prev and prev[-1].val==inorder[j]:
                    parent=prev.pop()
                    j+=1
                parent.right=x
            prev.append(x)
        return root


            






'''

keep adding left first preorder till we hit inorder

keep backtracking with inorder till we hit something new


we need a prev stack

we start by adding pre always to the left until we hit in
as we are doing that we are always appeding the the prev stack

now we start popping prev stack till the value stops matching in

keep going until we have hit the edn of pre index


'''

