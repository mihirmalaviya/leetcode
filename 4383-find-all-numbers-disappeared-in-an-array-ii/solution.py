class Solution:
    def findDisappearedNumbers(self, nums: list[int], lower: int, upper: int) -> list[list[int]]:

        nums.sort()
        res=[]


        start=lower
        for n in nums:
            if n<lower:
                continue

            if n>upper:
                if start<=upper:
                    res.append([start,upper])
                return res
            else:
                if start<=n-1:
                    res.append([start,n-1])
                start=n+1

        if start<=upper:
            res.append([start,upper])
        return res
                
                
