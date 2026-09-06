class Solution:
    def find132pattern(self, nums: List[int]) -> bool:

        n = len(nums)

        mins = [float("inf")]
        for i in range(n - 1):
            mins.append(min(mins[-1], nums[i]))

        s=[]
        for i in reversed(range(n)):
            while s and mins[i]>=s[-1]:
                s.pop()
            
            if s and s[-1]<nums[i]:
                return True
            s.append(nums[i])
                
        return False
        
