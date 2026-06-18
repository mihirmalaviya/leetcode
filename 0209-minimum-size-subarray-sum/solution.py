class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        res=float('inf')
        l,r=0,0
        total=0
        for r in range(len(nums)):
            total+=nums[r]
            while total>=target:
                res=min(res,r-l+1)
                if res==1:
                    return 1

                total-=nums[l]
                l+=1

        return 0 if res==float('inf') else res

