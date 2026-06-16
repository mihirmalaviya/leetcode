class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        c1,c2=set(nums1),set(nums2)
        return list(c1&c2)
