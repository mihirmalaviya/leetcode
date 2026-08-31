class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:


        res=[]

        def b(x):
            if x==len(nums):
                res.append(nums[:])
                
            for i in range(x,len(nums)):
                nums[i],nums[x]=nums[x],nums[i]
                b(x+1)
                nums[i],nums[x]=nums[x],nums[i]


        b(0)
        return res
