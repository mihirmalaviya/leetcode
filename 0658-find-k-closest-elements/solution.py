class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        
        res=[]

        l,r=0,len(arr)-1
        closest=float('inf')
        closesti=-1

        while l<=r:
            m=l+(r-l)//2

            if abs(arr[m]-x)<closest:
                closest=abs(arr[m]-x)
                closesti=m

            if arr[m]==x:
                break
            elif arr[m]<x:
                l=m+1
            else:
                r=m-1
        
        print(closesti)

        l=r=closesti

        for _ in range(k):
            
            if l-1>=0:
                behind=arr[l-1]
            else:
                r+=1
                continue
                
            if r<len(arr):
                forward=arr[r]
            else:
                l-=1
                continue
            
            if abs(behind-x)<=abs(forward-x):
                l-=1
            else:
                r+=1

        return arr[l:r]

