class Solution:
    def countGoodRotations(self, nums: list[int]) -> int:
        
        
        target=sum(nums)/2
        n=len(nums)
        k=n//2
        res=0
        
        curr=sum(nums[:k])
        for i in range(k,n+k):
            
            curr+=nums[i%n]
            curr-=nums[(i-k)%n]
            if curr>target:
                res+=1
                
        return res
