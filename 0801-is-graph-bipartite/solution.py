class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:

        n=len(graph)
        parent=list(range(n))
        
        def find(x):
            if x!=parent[x]:
                parent[x]=find(parent[x])
            return parent[x]

        def union(x,y):
            parent[find(x)]=find(y)

        for i,edges in enumerate(graph):
            for j in edges:
                if find(i)==find(j):
                    return False
                union(edges[0],j)

        return True
