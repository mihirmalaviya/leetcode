class Solution:
    def canFinish(self, numCourses: int, prereqs: List[List[int]]) -> bool:
        
        ind=[0 for i in range(numCourses)]
        post=[[] for i in range(numCourses)]
        
        for c,p in prereqs:
            ind[c]+=1
            post[p].append(c)
        

        s = [i for i in range(numCourses) if ind[i] == 0]
        visited = len(s)

        print(s)
       
        while s:
            i=s.pop()
            for p in post[i]:
                ind[p]-=1
                if ind[p]==0:
                    s.append(p)
                    visited+=1
        
        return visited==numCourses

            





