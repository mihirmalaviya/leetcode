class Solution:
    def jump(self, nums: List[int]) -> int:
        

        @cache
        def dp(i):
            if i>=len(nums)-1:
                return 0
            
            res=float('inf')
            for j in range(nums[i]):
                res=min(res,1+dp(i+j+1))

            return res
        
        return dp(0)



