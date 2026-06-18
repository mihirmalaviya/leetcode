class Solution:
    def generateValidStrings(self, n: int, k: int) -> list[str]:

        res=[]
        q=deque([('',0)])

        while q:
            for _ in range(len(q)):
                s,c=q.popleft()
                if len(s)==n:
                    res.append(s)
                    continue
                q.append((s+"0",c))
                c+=len(s)
                if c<=k and (not s or s[-1]!="1"):
                    q.append((s+"1",c))

        return res

        

