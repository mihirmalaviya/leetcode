"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        
        clones={}
        def clone(n):
            if not n:
                return None
            if n in clones:
                return clones[n]
            
            c=Node(n.val)
            clones[n]=c
            c.neighbors=[clone(x) for x in n.neighbors]

            return c
        
        return clone(node)

