class Solution:
    def countValidSubarrays(self, nums: list[int], x: int) -> int:

        n=len(nums)
        res=0
        chx=str(x)
            
        p = [0] * (n + 1)
        for i in range(n):
            p[i+1] = p[i] + nums[i]
            
        for l in range(n):
            for r in range(l,n):
                sum=p[r+1]-p[l]
                if sum%10==x:
                    if str(sum)[0]==chx:
                        res+=1
        return res

