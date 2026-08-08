class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        

        for r in range(len(nums)):
            if nums[r]>0:
                break
        
        l=r-1

        res=[]
        while l>=0 or r<len(nums):
            if l>=0 and r<len(nums):
                if abs(nums[l])<abs(nums[r]):
                    res.append(nums[l]**2)
                    l-=1
                else:
                    res.append(nums[r]**2)
                    r+=1
            elif l>=0:
                res.append(nums[l]**2)
                l-=1
            else:
                res.append(nums[r]**2)
                r+=1

        return res



