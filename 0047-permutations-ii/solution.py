class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        
        res=[]
        # nums.sort()
        used=defaultdict(bool)

        def b(i):
            if i==len(nums):
                res.append(nums[:])

            for j in range(i,len(nums)):
                if used[j]:
                    continue
                if j>0 and nums[j-1]==nums[j] and not used[j-1]:
                    continue
                used[i]=True
                nums[i],nums[j]=nums[j],nums[i]
                b(i+1)
                used[i]=False
                nums[i],nums[j]=nums[j],nums[i]

        b(0)
        return list(set([tuple(x) for x in res]))
        # return res
