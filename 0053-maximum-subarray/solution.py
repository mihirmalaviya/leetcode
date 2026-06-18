class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        res=float('-inf')
        currmax=0
        for n in nums:
            currmax=max(n,currmax+n)
            res=max(currmax,res)
        return res
        
