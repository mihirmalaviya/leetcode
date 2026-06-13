class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:

        buckets={}
        
        l=0
        for r in range(len(nums)):
            if r>indexDiff: 
                i=nums[l]//(valueDiff+1)
                del buckets[i]
                l+=1
            
            i=nums[r]//(valueDiff+1)
            if i in buckets:
                return True
            elif i+1 in buckets and abs(buckets[i+1]-nums[r])<=valueDiff:
                return True
            elif i-1 in buckets and abs(buckets[i-1]-nums[r])<=valueDiff:
                return True
            else:
                buckets[i]=nums[r]

        return False
            


        


'''

sliding window

we can have buckets of size valueDiff+1

at any point each bucket must only have at max one thing, because if it has more than one then that means ajdkaljsdkah

each time adding to a bucket manually check the next to it buckets

'''

