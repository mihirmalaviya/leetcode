class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dpi=defaultdict(int)
        dpi[0]=1

        for i in range(len(nums)):
            dpi1=defaultdict(int)
            for total, count in dpi.items():
                dpi1[total-nums[i]] += count
                dpi1[total+nums[i]] += count
            dpi=dpi1

        return dpi[target]


        # @cache
        # def dp(i,x):
        #     if i==len(nums):
        #         return 1 if x==0 else 0
            
        #     take=0
        #     skip=dp(i+1,x+nums[i])
        #     take=dp(i+1,x-nums[i])
            
        #     return skip+take

        # return dp(0,target)
