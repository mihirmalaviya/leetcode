class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        s=sum(nums)
        if (s%2): return False
        s=s//2

        n=len(nums)

        dp=[[False]*(s+1) for _ in range(n+1)]

        for i in range(n+1):
            dp[i][0]=True

        for i in range(1,n+1):
            for j in range(1,s+1):
                dp[i][j]=dp[i-1][j]

                if j>=nums[i-1] and dp[i-1][j-nums[i-1]]:
                    dp[i][j]=True
                
        return dp[-1][-1]
