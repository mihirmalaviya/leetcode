class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        

        prev=nums[0]
        curr=None
        run=0
        res=0
        for n in nums[1:]:
            if curr==prev-n:
                run+=1
            else:
                res+=(run+1)*run//2
                run=0
            curr=prev-n
            prev=n

        if run: res+=(run+1)*run//2

        return res

    
