class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        parent=[i for i in range(len(edges)+1)]

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])

            return parent[x]

        def union(x,y):
            a=find(x)
            b=find(y)
            if a==b:
                return True
            else:
                parent[a]=b
                return False
        
        for a,b in edges:
            if union(a,b):
                return [a,b]

