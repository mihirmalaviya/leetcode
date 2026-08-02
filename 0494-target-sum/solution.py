class Solution(object):
    def findTargetSumWays(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        self.memo = {}
        return self.dp(nums,target,len(nums)-1,0)

    def dp(self,nums,target,i,curr_sum):
        if (i,curr_sum) in self.memo:
            return self.memo[(i,curr_sum)]
        if i<0 and curr_sum==target:
            return 1
        if i<0: 
            return 0

        pos=self.dp(nums,target,i-1,curr_sum+nums[i])
        neg=self.dp(nums,target,i-1,curr_sum-nums[i])
        
        self.memo[(i,curr_sum)]=pos+neg
        return pos+neg
