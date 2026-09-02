# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

class Solution:
    def findInMountainArray(self, target: int, mountainArr: 'MountainArray') -> int:

        n=mountainArr.length()
        l=0
        r=n-1
        currmax=0
        maxi=0
        while l<=r:
            m=l+(r-l)//2
            a=mountainArr.get(m)
            b=-1 if m+1==n else mountainArr.get(m+1)
            if b==-1:
                left=False
            else:
                left=a<b
            
            if a>currmax:
                maxi=m
                currmax=a
            if b>currmax:
                maxi=m+1
                currmax=b

            if left:
                l=m+1
            else:
                r=m-1
        

        if currmax<target:
            return -1
        if currmax==target:
            return maxi
            
        l=0
        r=maxi
        while l<=r:
            m=l+(r-l)//2
            x=mountainArr.get(m)
            if x==target:
                return m
            elif x<target:
                l=m+1
            else:
                r=m-1
        
        l=maxi+1
        r=mountainArr.length()-1
        while l<=r:
            m=l+(r-l)//2
            x=mountainArr.get(m)
            if x==target:
                return m
            elif x<target:
                r=m-1
            else:
                l=m+1

        return -1
