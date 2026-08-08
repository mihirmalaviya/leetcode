class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        
        l=max(weights)
        r=sum(weights)

        def works(c):

            d=0
            curr=c
            for w in weights:
                if curr>=w:
                    curr-=w
                else:
                    d+=1
                    curr=c-w

            return d+1
            
        res=-1
        while l<=r:
            m=l+(r-l)//2
            d=works(m)
            if d<=days:
                r=m-1
                res=m
            else:
                l=m+1
        return res

