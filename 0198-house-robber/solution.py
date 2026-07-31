class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # memo=[-1]*len(nums)
        # def dfs(i,memo=memo):
        #     if i<0:
        #         return 0
        #     if memo[i]!=-1:
        #         return memo[i]
        #     memo[i]=max(dfs(i-2)+nums[i],dfs(i-1))
        #     return memo[i]
        # return dfs(len(nums)-1)

        a=0
        b=nums[0]

        for i in range(1,len(nums)):
            a=max(b,a+nums[i])
            a,b=b,a

        return b




            

