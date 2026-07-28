class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        
        res=0
        l=0
        r=len(height)-1
        maxl=height[l]
        maxr=height[r]

        while l<r:
            if height[l]<height[r]:
                res+=max(0,min(maxl,maxr)-height[l])
                l+=1
                maxl=max(maxl,height[l])
            else:
                res+=max(0,min(maxl,maxr)-height[r])
                r-=1
                maxr=max(maxr,height[r])

        return res
