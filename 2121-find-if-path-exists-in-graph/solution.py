class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        if source==destination:
            return True

        parent=[i for i in range(n)]

        def find(x):
            if parent[x]!=x:
                parent[x]=find(parent[x])
            return parent[x]

        def union(x,y):
            a,b=find(x),find(y)
            if a==b:
                return True

            parent[a]=b
            return False
        
        for a,b in edges:
            union(a,b)
        
        return find(source)==find(destination)
        
