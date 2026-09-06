class Solution:
    def canSeePersonsCount(self, heights: List[int]) -> List[int]:
        
        s=[]
        res=[]
        for i in range(len(heights)):
            h=heights.pop()
            i=0
            while s and s[-1]<h:
                s.pop()
                i+=1
            
            res.append(i+ (1 if s else 0))
            s.append(h)
        res.reverse()
        return (res)
        
