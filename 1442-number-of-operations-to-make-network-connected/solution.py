class Solution:
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        
        parents=list(range(n))

        def find(x):
            if x!=parents[x]:
                parents[x]=find(parents[x])

            return parents[x]

        def union(x,y):
            '''returns true if they are already unioned'''
            a,b=find(x),find(y)
            if a==b:
                return True
            else:
                parents[a]=b
                return False
        
        redundant=0
        x=n
        for a,b in connections:
            if union(a,b):
                redundant+=1
            else:
                x-=1
        
        # print(x,redundant)

        return x-1 if redundant>=x-1 else -1

