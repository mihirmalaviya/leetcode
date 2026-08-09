class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        target=sum(nums)//2
        if target!=sum(nums)/2:
            return False

        dp=[False]*(target+1)
        dp[0]=True

        for i in reversed(range(len(nums))):
            for x in reversed(range(nums[i],target+1)):
                dp[x] = dp[x] or dp[x-nums[i]]
                if dp[target]: return True
        
        return dp[target]

        # def dp(i,x):
            
        #     take=False
        #     skip=dp(i+1,x)
        #     if nums[i]<=x:
        #         take=dp(i+1,x-nums[i])

        #     return skip or take

        # return dp(0,target)
