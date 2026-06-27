# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        
        :type root: TreeNode
        :rtype: str
        """

        res=[]
        q=deque([root])
        while q:
            for _ in range(len(q)):
                n=q.popleft()
                if n:
                    res.append(str(n.val))
                else:
                    res.append('')
                    continue
                q.append(n.left)
                q.append(n.right)
        res.pop()
        return ",".join(res)
        

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:return
        nodes=data.split(",")
        print(nodes)

        root=TreeNode(int(nodes[0]))
        q=deque([root])
        i=1
        while q:
            curr=q.popleft()
            if i<len(nodes) and nodes[i]: 
                curr.left=TreeNode(int(nodes[i]))
                q.append(curr.left)
            i+=1
            if i<len(nodes) and nodes[i]: 
                curr.right=TreeNode(int(nodes[i]))
                q.append(curr.right)
            i+=1

        return root


        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
