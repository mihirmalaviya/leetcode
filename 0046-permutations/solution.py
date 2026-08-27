class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res=[]

        def b(s):
            if s==len(nums):
                res.append(nums[:])

            for i in range(s,len(nums)):
                nums[s],nums[i]=nums[i],nums[s]
                b(s+1)
                nums[s],nums[i]=nums[i],nums[s]
        
        b(0)
        return res

