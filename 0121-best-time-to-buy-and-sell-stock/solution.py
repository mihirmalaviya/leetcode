class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        currmin=float('inf')
        res=0
        for p in prices:
            currmin=min(p,currmin)
            res=max(res, p-currmin)
        return res
 
