class Solution(object):
    def subarraysWithKDistinct(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        if not k: return 0
        
        # p=[0]
        # seen=set()
        # for num in nums:
        #     if not num in seen:
        #         seen.add(num)
        #     p.append(len(seen))
        
        # print(p)
        # l=fl=1
        # for r in range(1,len(p)):
        #     while l+1<r and p[r]-p[l+1]>k:
        #         l+=1
        #     while fl+1<r and p[r]-p[fl+1]>=k:
        #         fl+=1

        #     print(l,fl,r, p[r]-p[fl])

        res=0
        seen=defaultdict(int)
        l=0
        for r in range(len(nums)):
            seen[nums[r]]+=1
            while l<r and len(seen)>k:
                seen[nums[l]]-=1
                if seen[nums[l]]==0:
                    del seen[nums[l]]
                l+=1

            if len(seen)<=k:
                res+=r-l+1

        k-=1
        seen.clear()
        l=0
        for r in range(len(nums)):
            seen[nums[r]]+=1
            while l<r and len(seen)>k:
                seen[nums[l]]-=1
                if seen[nums[l]]==0:
                    del seen[nums[l]]
                l+=1

            if len(seen)<=k:
                res-=r-l+1
        return res
           




