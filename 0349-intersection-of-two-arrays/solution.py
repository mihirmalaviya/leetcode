class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        if nums1<nums2:
            nums1,nums2=nums2,nums1
        
        nums1.sort()
        res=[]
        for target in set(nums2):
            l=0
            r=len(nums1)-1
            while l<=r:
                m=l+(r-l)//2
                x=nums1[m]
                if x==target:
                    res.append(target)
                    break
                elif x<target:
                    l=m+1
                else:
                    r=m-1
        return res

