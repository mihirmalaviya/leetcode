class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        
        stones=[-s for s in stones]
        heapify(stones)

        while stones:
            if len(stones)==1:
                return -stones[0]
            
            y=heappop(stones)
            x=heappop(stones)
            if x!=y:
                heappush(stones,y-x)

        return 0
