class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=max(sum(piles)//h,1)
        r=max(piles)
        def check(k):
            return sum(math.ceil(x/k) for x in piles)<=h
        return l+bisect.bisect_left(range(l,r), True, key=check)
 
