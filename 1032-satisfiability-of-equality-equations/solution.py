class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:

        parent={}
        def find(x):
            if x not in parent:
                return x

            if x!=parent[x]:
                parent[x]=find(parent[x])
            return parent[x]

        def union(x,y):
            if x not in parent:
                parent[x]=x
            if y not in parent:
                parent[y]=y
            a,b=find(x),find(y)
            if a==b:
                return True
            parent[a]=b
            return False


        for eq in equations:
            if '==' in eq:
                union(eq[0],eq[-1])

        for eq in equations:
            if '!=' in eq:
                if find(eq[0]) == find(eq[-1]):
                    return False
        return True
            
