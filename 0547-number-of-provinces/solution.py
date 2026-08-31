class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:

        parents=list(range(len(isConnected)))
        
        def find(x):
            if x!=parents[x]:
                parents[x]=find(parents[x])
            return parents[x]

        def union(x,y):
            a,b=find(x),find(y)
            if a==b:
                return True
            else:
                parents[a]=b
                return False
        
        n=len(parents)
        for i,c in enumerate(isConnected):
            if c==i:
                continue
            for j,x in enumerate(c):
                if x:
                    if not union(i,j):
                        n-=1

        return n
            
        
