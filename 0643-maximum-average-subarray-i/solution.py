class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:


        res=-float('inf')
        total=0
        l=0
        for r in range(len(nums)):
            total+=nums[r]

            if r>=k-1:
                res=max(res,total)
                total-=nums[l]
                l+=1
                
        return res/k

            


        # curr=0
        # till=0

        # for n in nums:
        #     curr=max(n+curr,n)
        #     till=max(curr,till)
            
        # return till
        


