class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        i=0
        n=len(nums)
        maxq=deque()
        res=[]
        while i<n:
            curr=nums[i]
            while maxq and maxq[0][1]<=i-k:
                maxq.popleft()
            while maxq and maxq[-1][0]<=curr:
                maxq.pop()
            maxq.append((curr,i))
            # print(maxq)
            if i+1>=k:
                res.append(maxq[0][0])
            i+=1
            
        # print(res)
        return res
                

'''

'''
