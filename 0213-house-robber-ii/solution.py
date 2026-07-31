class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums)==1:return nums[0]
        
        return max(self.srob(nums[:-1]), self.srob(nums[1:]))

    def srob(self,nums):
        a=0
        b=nums[0]
        for i in range(1,len(nums)):
            a=max(b,a+nums[i])
            a,b=b,a
        return b
