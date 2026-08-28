class Solution:
    def jump(self, nums: List[int]) -> int:

        for i in range(1,len(nums)):
            nums[i]=max(i+nums[i],nums[i-1])
        
        res=0
        i=0
        while i<len(nums)-1:
            i=nums[i]
            res+=1

        return res
