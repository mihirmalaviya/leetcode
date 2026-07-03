class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        nums.sort()

        l,r=0,1
        pairs=set()

        while r<len(nums):
            total=nums[r]-nums[l]
            if total==k and l!=r:
                pairs.add((nums[l], nums[r])) 
                l+=1
                r+=1
            elif total<k:
                r+=1
            else:
                l+=1

            if l==r:
                r+=1
        return len(pairs)



        return len(pairs)
                


