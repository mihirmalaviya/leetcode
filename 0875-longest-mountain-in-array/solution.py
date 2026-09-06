class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        
        n=len(arr)
        left=[1]*n
        right=[1]*n

        for i in range(1,n):
            if arr[i]>arr[i-1]:
                left[i]+=left[i-1]

        for i in reversed(range(0,n-1)):
            if arr[i]>arr[i+1]:
                right[i]+=right[i+1]
        
        # print(left,right)
        
        res=0
        for l,r in zip(left,right):
            if l>1 and r>1:
                res=max(res,l+r-1)
        return res
