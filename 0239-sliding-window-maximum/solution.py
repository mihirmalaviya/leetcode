class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        
        res=[]

        q=deque()   

        for i,n in enumerate(nums):
            while q and n>q[-1]:
                q.pop()

            if not q or q[-1]>=n:
                q.append(n)

            prev=i-k

            if prev>=0:
                if q[0]==nums[prev]:
                    q.popleft()
            if prev>=-1:
                res.append(q[0])


        return res


