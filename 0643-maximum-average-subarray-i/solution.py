class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        
        sum=0
        l,r=0,0
        for r in range(k):
            sum+=nums[r]
        
        currmax = sum
        while r<len(nums)-1:
            r+=1
            sum+=nums[r]
            sum-=nums[l]
            l+=1
            currmax = max(sum, currmax)
        
        return currmax/k

