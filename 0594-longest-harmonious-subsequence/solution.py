class Solution(object):
    def findLHS(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        # l=0
        # res=0
        # counts=Counter()
        # for r in range(len(nums)):
        #     counts[nums[r]]+=1
            
        #     while len(counts)>2:
        #         counts[nums[l]]-=1
        #         if counts[nums[l]]<=0:
        #             del counts[nums[l]]
        #         l+=1

        #     if len(counts)==2:
        #         res=max(res,r-l+1)
        #         print(res)
        # return res
        counts=Counter(nums)

        res=0
        for n in counts:
            if n-1 in counts:
                res=max(res,counts[n]+counts[n-1])
        return res

