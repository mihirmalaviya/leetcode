class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res=[]
        def dfs(curr, nums):
            if len(curr)==len(nums):
                res.append(curr[:])
                return
            
            for i in range(len(nums)):
                if nums[i] in curr: continue
                curr.append(nums[i])
                dfs(curr,nums)
                curr.pop()
        

        dfs([],nums)
        return res
