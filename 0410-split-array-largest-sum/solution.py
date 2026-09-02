class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:
        
        def check(cap):
            c=0
            i=1
            for n in nums:
                c+=n
                if c>cap:
                    i+=1
                    c=n

            print(cap,i)
            return i<=k
        
        l=max(nums)
        r=sum(nums)
        best=-1
        while l<=r:
            m=l+(r-l)//2
            
            if check(m):
                best=m
                r=m-1
            else:
                l=m+1

        return best

            

