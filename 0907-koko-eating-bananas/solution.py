class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def ok(k):
            if k==0: return False
            total=0
            for b in piles:
                total+=b//k
                if b%k:
                    total+=1
            return total<=h

        l,r=1,max(piles)
        res=0

        while l<=r:
            m=l+(r-l)//2
            if ok(m):
                res=m
                r=m-1
            else:
                l=m+1

        return res
