class Solution:
    def canJump(self, nums: List[int]) -> bool:
        
        @cache
        def dp(i):
            if i+1>=len(nums):
                return True

            res = False
            for j in range(nums[i]):
                res |= dp(i+j+1)
                if res==True:
                    return True

            return False
        
        return dp(0)
            






'''
        GREEDY

        furthest=0

        for i in range(len(nums)):
            if i>furthest:
                return False
            furthest=max(furthest,i+nums[i])

        return True
'''
