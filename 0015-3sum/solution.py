class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        
        nums.sort()

        res=set()
        prev=nums[0]
        for k in range(len(nums)):
            if k>0 and nums[k]==nums[k-1]:
                continue
            
            l,r=k+1,len(nums)-1
            if l==k: l+=1
            if r==k: r-=1
            while l<r:
                total=nums[l]+nums[r]
                if total<-nums[k]:
                    l+=1
                elif total>-nums[k]:
                    r-=1
                else:
                    # print(l,r,k)
                    res.add(tuple(sorted([nums[l],nums[r],nums[k]])))
                    l+=1
                    r-=1
                    while l<r and nums[l]==nums[l-1]:
                        l+=1
                    while l<r and nums[r]==nums[r+1]:
                        r-=1

                if l==k: l+=1
                if r==k: r-=1

        return [[a,b,c] for a,b,c in sorted(list(res))]

