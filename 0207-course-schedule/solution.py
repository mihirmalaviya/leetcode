class Solution:
    def canFinish(self, numCourses: int, prereqs: List[List[int]]) -> bool:
        
        pre={i:[] for i in range(numCourses)}
        
        for c,p in prereqs:
            pre[c].append(p)
        
        visited=set()
        def dfs(c):
            if c in visited:
                return False
            if not pre[c]:
                return True

            visited.add(c)
            for p in pre[c]:
                if dfs(p)==False:
                    return False
            visited.remove(c)
            pre[c]=[]
            return True
        
        for c,p in prereqs:
            if not dfs(c):
                return False
        return True



