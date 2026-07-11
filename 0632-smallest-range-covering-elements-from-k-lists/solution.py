class Solution:
    def smallestRange(self, nums: List[List[int]]) -> List[int]:
        

        h=[]
        hi=float('-inf')
        res=[]
        mindist=float('inf')
        for j in range(len(nums)):
            l=nums[j]
            hi=max(hi,l[0])
            heappush(h, (l[0],0,j))
        
        while 1:
            lo,x,y = heappop(h)
            l=nums[y]
            if hi-lo<mindist:
                mindist=hi-lo
                res=[lo,hi]
            
            if x+1>=len(l):
                break
            
            hi=max(hi,l[x+1])
            heappush(h,(l[x+1],x+1,y))

        return res
