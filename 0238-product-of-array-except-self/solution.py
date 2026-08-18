class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        pre=[0]*len(nums)
        post=[0]*len(nums)
        pre[0]=1
        post[-1]=1

        for i in range(1,len(nums)):
            pre[i]=pre[i-1]*nums[i-1]
        for i in reversed(range(len(nums)-1)):
            post[i]=post[i+1]*nums[i+1]

        # print(pre,post)

        res=[0]*len(nums)
        for i in range(len(nums)):
            res[i]=pre[i]*post[i]
        
        return res

        

        

