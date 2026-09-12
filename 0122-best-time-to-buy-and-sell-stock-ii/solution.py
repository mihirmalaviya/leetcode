class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        
        res=0
        cur=prices[0]
        for p in prices:
            if cur<p:
                res+=p-cur
            cur=p
        return res



'''
[7,1,5,3,6,4]
[1,5,3,6]

'''
