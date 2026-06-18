class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        def rec(nums, target, l,r):
            if not l<=r:
                return -1

            m=l+(r-l)//2
            if nums[m]==target:
                return m

            elif nums[m]>target:
                return rec(nums, target, l,m-1)
            elif nums[m]<target:
                return rec(nums, target, m+1,r)
        
        return rec(nums,target,0,len(nums)-1)
