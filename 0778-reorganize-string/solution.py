class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter([ch for ch in s])
        h=[(-v,k) for k,v in counts.items()]
        heapify(h)
        res=[]

        prevc, prevch = 0, ''
        while h:
            c,ch=heappop(h)
            res.append(ch)
            if prevc<0:
                heappush(h, (prevc,prevch))
            c+=1
            prevc,prevch=c,ch
        res = ''.join(res)
        if len(res)!=len(s):return ""
        return res
            
