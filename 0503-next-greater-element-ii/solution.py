class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        n=len(nums)
        res=[-1]*n
        s=[]
        nums.extend(nums)
        for i in reversed(range(n)):
            x=nums.pop()
            while s and x>=s[-1]:
                s.pop()
            
            res[i]=s[-1] if s else -1
            s.append(x)
        
        for i in reversed(range(n)):
            x=nums.pop()
            while s and x>=s[-1]:
                s.pop()
            
            res[i]=s[-1] if s else -1
            s.append(x)
        
        return res
