class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        travel=set(days)
        
        dp=[0]*366

        for i in range(1,366):
            if not i in travel:
                dp[i]=dp[i-1]
            else:
                dp[i]=dp[i-1]+costs[0]
                dp[i]=min(dp[i],dp[max(0,i-7)]+costs[1])
                dp[i]=min(dp[i],dp[max(0,i-30)]+costs[2])
        
        return dp[-1]

