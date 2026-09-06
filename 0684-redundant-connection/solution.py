class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent = [i for i in range(len(edges)+1)]

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            
            return parent[x]

        def union(x,y):
            a,b=find(x),find(y)
            if a!=b:
                parent[a]=b
                return False
            return True
            
        for a,b in edges:
            if union(a,b):
                return [a,b]


