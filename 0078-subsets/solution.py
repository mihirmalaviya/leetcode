class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res=[]

        def dfs(curr,i):
            if i==len(nums):
                res.append(curr[:])
                return

            curr.append(nums[i])
            dfs(curr,i+1)

            curr.pop()
            dfs(curr,i+1)
        
        dfs([],0)
        return res


