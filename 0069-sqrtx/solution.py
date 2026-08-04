class Solution:
    def mySqrt(self, x: int) -> int:
        
        l=1
        r=x
        while l<=r:
            m=l+(r-l)//2
            
            mm=m*m
            if mm==x:
                return m
            elif mm<x:
                l=m+1
            elif mm>x:
                r=m-1
        return r

