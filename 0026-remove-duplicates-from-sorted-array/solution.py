class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if len(nums) == 1: return 1
        
        l=0
        prev=None
        for r in range(len(nums)):
            if nums[r]!=prev:
                nums[l]=nums[r]
                l+=1
            prev=nums[r]
        return l





