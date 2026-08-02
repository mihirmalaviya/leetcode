class Solution:
    def numSquares(self, n: int) -> int:
        
        dp=[n]*(n+1)
        dp[0]=0

        for target in range(1,n+1):
            for x in range(1,target+1):
                s=x*x
                if target-s<0:
                    break
                dp[target]=min(dp[target],1+dp[target-s])

        return dp[n]
