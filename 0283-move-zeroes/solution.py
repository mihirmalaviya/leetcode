class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        
        l=0
        for r in range(len(nums)):
            x=nums[r]
            nums[r]=0
            if x!=0:
                nums[l]=x
                l+=1
        
