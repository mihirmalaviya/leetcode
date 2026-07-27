class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        k=len(nums)/2
        counts=Counter()
        for num in nums:
            counts[num]+=1
            if counts[num]>k:
                return num 
        return None

        
