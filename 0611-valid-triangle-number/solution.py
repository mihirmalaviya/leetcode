class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        
        nums.sort()
        res=0

        for k in reversed(range(len(nums))):
            r=k-1
            l=0

            while l<r:
                if nums[l]+nums[r]>nums[k]:
                    res+=r-l
                    r-=1
                else:
                    l+=1
            
        return res



