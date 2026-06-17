class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
       
        numset=set(nums)
        res=0
        for n in numset:
            if not n-1 in numset:
                i=0
                while n+i in numset:
                    i+=1
                res=max(res,i)

        return res

 
