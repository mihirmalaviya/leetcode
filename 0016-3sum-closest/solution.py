class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        if len(nums)==3:return sum(nums)
        
        nums.sort()
        print(nums)
        
        res=float('inf')
        for i in range(len(nums)):
            l,r=0,len(nums)-1
            while l<r:
                if l==i: l+=1
                if r==i: r-=1
                if l==r: break

                # print(i,l,r)   

                total = nums[l]+nums[r]+nums[i]

                if abs(res-target)>abs(total-target): 
                    # print(i,l,r)   
                    res=total

                if total-target==0:
                    return total
                elif total>target: # too big
                    r-=1
                else:
                    l+=1

        return res


        
'''
l,r=0,len(nums)-1

if a+b+c is too big set

'''

