class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        
        res=0
        total=0
        seen={0:1}
        for n in nums:
            total+=n
            if total-k in seen:
                res+=seen[total-k]

            if total in seen:
                seen[total]+=1
            else:
                seen[total]=1

        return res
