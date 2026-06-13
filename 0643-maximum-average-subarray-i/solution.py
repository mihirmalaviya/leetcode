class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:

        res=float('-inf')
        l=0
        total=0
        for r in range(len(nums)):
            total+=nums[r]
            if r>=k:
                total-=nums[l]
                l+=1
            if r+1>=k:
                res=max(res,total/k)

            
        return res

            


        # curr=0
        # till=0

        # for n in nums:
        #     curr=max(n+curr,n)
        #     till=max(curr,till)
            
        # return till
        


