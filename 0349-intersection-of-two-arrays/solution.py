class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        res=[]
        for n in nums1:
            if n in nums2 and not n in res:
                res.append(n)
        
        return res
