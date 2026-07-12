class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        
        h=list(Counter(words).items())
        h=[(-j,i) for i,j in h]
        heapify(h)
        res=[]
        for i in range(k):
            res.append(heappop(h)[1])
        return res

