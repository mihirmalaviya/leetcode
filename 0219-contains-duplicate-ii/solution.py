class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        counts=defaultdict(int)
        l=0
        for r in range(len(nums)):
            if r>k:
                counts[nums[l]]-=1
                l+=1
            n=nums[r]
            if counts[n]>0: return True
            counts[n]+=1
        
        return False
            

            
