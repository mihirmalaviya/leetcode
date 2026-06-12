class Solution:
    def containsNearbyAlmostDuplicate(self, nums: List[int], indexDiff: int, valueDiff: int) -> bool:
        

        buckets={}
        l=0
        for r in range(len(nums)):
            num=nums[r]

            if r>indexDiff:
                i=nums[l]//(valueDiff+1)
                del buckets[i]
                l+=1

            i=num//(valueDiff+1)
            # print(buckets,i)
            if i in buckets: # its close enough
                return True
            elif i+1 in buckets and abs(buckets[i+1]-num)<=valueDiff or i-1 in buckets and abs(buckets[i-1]-num)<=valueDiff:
                return True
            else:
                buckets[i]=num
        return False


'''

sliding window

when r goes up we add it to a bucket based on it // valuedif

when l goes up we remove it from the bucket (popleft)

then we either have the 2 things in one bucket or in 2 adj buckets

since we did it in order both are sorted and we can do a 2 pointer thingy to figure out if they have close index to eachotehr? maybe by making them into 1 sorted array and checking like that

'''

