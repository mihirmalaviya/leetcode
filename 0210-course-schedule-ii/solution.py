class Solution:
    def findOrder(self, numCourses: int, prereqs: List[List[int]]) -> List[int]:
        
        adj={i:[] for i in range(numCourses)}
        for c,p in prereqs:
            adj[c].append(p)

        res=[]
        cycle=set()
        visited=set()
        def dfs(c):
            if c in cycle:
                return False
            if c in visited:
                return True

            cycle.add(c)
            for x in adj[c]:
                if not dfs(x):
                    return False
            cycle.remove(c)

            visited.add(c)
            res.append(c)
            return True
         
        for c in range(numCourses):
            if not dfs(c):
                return []

        return res
