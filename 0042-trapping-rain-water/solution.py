class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        lm,rm=0,0
        l,r=0,len(height)-1
        while l<r:
            lh,rh = height[l],height[r]
            lm,rm=max(lh,lm),max(rh,rm)
            mh=min(lm,rm)
        
            if lh<rh:
                l+=1
                h=height[l]
            else:
                r-=1
                h=height[r]

            if mh>h:
                res+=mh-h
            
            # print(mh,h)

        return res
 
